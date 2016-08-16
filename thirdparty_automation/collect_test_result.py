import os
import sys
import subprocess
from adb_android import adb_android
import record_logcat

def pull_logs(test_name, log):
	print 'collecting logs......'
	#make new test directory
	newpath = 'C:\Workspace\_temp\%s' %(test_name)
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	#pull video
	adb_android.pull('sdcard/%s.mp4' %(test_name), newpath) 
	#dump log to test
	logfile = open('C:\Workspace\_temp\logcat.txt','a')
	for item in log:
		logfile.write("%s\n" %(item))	
	logfile.close()

