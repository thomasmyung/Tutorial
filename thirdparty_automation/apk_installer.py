from adb_android import adb_android
import subprocess
import os
import sys

def apk_install(apk_name):
	if apk_name[0].endswith('.apk'):
		install_output = adb_android.install('E:\Automation2\%s' %(apk_name[0]))	
		if 'Success' in install_output[1]:
			return True
		else :
			failed_output = install_output[1]
			c = failed_output.split('\n')
			
			#create txt file with install failure message
			f = open('E:\Automation2\install_error.txt','w')
			f.write(c[len(c)-2])
			f.close
			print c[len(c)-2]
			return False
	else:
		print'upload proper apk file with extension .apk'
		
		#create txt file to notify there was an error
		f = open('E:\Automation2\error.txt','w')
		f.write('upload proper apk file with extension .apk')
		f.close


