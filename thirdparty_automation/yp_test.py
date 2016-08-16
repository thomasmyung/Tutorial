import os
import sys
import subprocess
import time
from adb_android import adb_android

class Yp_Test(object):
	def __init__(self, search_keyword="", location=""):
		self.search_keyword = search_keyword
		self.location = location

	def __str__(self):
		return '%s, %s' %(self.search_keyword, self.location)

	def print_yp(yp):
		print '%s, %s' %(yp.search_keyword, yp.location)

	def yp_launch_app(self):
		adb_android.shell('monkey -p com.yellowpages.android.ypmobile -c android.intent.category.LAUNCHER 1')

	def yp_close_app(self):
		adb_android.shell('am force-stop com.yellowpages.android.ypmobile')

	def yp_search_business(self):
		adb_android.shell('am force-stop com.yellowpages.android.ypmobile')
		adb_android.shell('monkey -p com.yellowpages.android.ypmobile -c android.intent.category.LAUNCHER 1')
		time.sleep(5)
		adb_android.shell('input keyevent 66')
		time.sleep(3)
		adb_android.shell('input keyevent 66')
		time.sleep(1)
		adb_android.shell('input keyevent 61')
		j =0
		while j < len(self.search_keyword):
			if (self.search_keyword[j] != ' '):
				adb_android.shell('input keyevent KEYCODE_%s' %(self.search_keyword[j].upper()))
			elif (self.search_keyword[j] == ' '):
				adb_android.shell('input keyevent KEYCODE_SPACE')
			j += 1
		adb_android.shell('input keyevent 20')
		k =0
		while k < len(self.location):
			if (self.location[k] != ' '):
				adb_android.shell('input keyevent KEYCODE_%s' %(self.location[k].upper()))
			elif (self.location[k] == ' '):
				adb_android.shell('input keyevent KEYCODE_SPACE')
			k +=1
		adb_android.shell('input keyevent 66')
		time.sleep(7)
		adb_android.shell('input tap 252.773 1263.750')




#yptest = Yp_Test('pizza hut', 'Bellevue WA')
#yptest.yp_search_business()