import os, time
import device_watcher
import sys
import os
import threading
import time
import subprocess
import device_watcher
import apk_installer
import yp_test
import yp_test_execute
import screen_record
import record_logcat
import collect_test_result

class AdbWrapper(object):
	def __init__(self):
		super(AdbWrapper, self).__init__()

	def shell(self, *args):
		for args in args:
			print (args)
		p = subprocess.call(args, shell=True)
	def startlogging(self, storage, deviceid):
		logcatcmd = 'adb logcat -b main -b system -b radio -v time'
		t = threading.Thread(target=storage.record, args=([logcatcmd],))
		t.start()

path_to_watch = "E:\Automation2"
file_list = []
adbwrapper = AdbWrapper()

before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:

  time.sleep (10)
  print(threading.active_count())
  #check for connected devices  
  device_id = device_watcher.get_deviceid()
  print device_id
  devicemodel_list=[]
  device_watcher.get_device_model(device_id)
 

  #check for file added/removed
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: 
  	
  	print "Added: ", ", ".join (added)
  	file_list.append(added[0])
  	#verify if it's has .apk extension and install the deivice
  	apkinstall = apk_installer.apk_install(added)
  	
	#upon successful intall, initiate 10776 yp testing 
  	if apkinstall == True:
  		yptest = yp_test.Yp_Test('hamburger','bellevue')
  		#start screen record for test #1
  		yp_screen_record = threading.Thread(target=screen_record.screenrecord, args=['120', 'test1.mp4'])
  		yp_screen_record.start()
  		time.sleep(1)
  		
  		#start logging
  		yp_logcat = record_logcat.LogStorage()
  		adbwrapper.startlogging(yp_logcat, device_id)
  		time.sleep(1)

  		yp_logcat = []
  		time.sleep(5)
  		print yp_logcat
  		yp_test_execute.execute_test1(yptest)

  		collect_test_result.pull_logs('test1', yp_logcat)
  		#yp_screen_record2 = threading.Thread(target=screen_record.screenrecord, args=['40', 'test2.mp4'])
  		#yp_screen_record2.start()
  		print(threading.active_count())


  
  	#delte file upon test exexution
  	if added[0] == 'error.txt':
  		pass
  	elif added[0]== 'install_error.txt':
  		pass
  	else:
  		os.remove("%s\%s" %(path_to_watch,added[0]))


  if removed: 
  	print "Removed: ", ", ".join (removed)
  before = after


  