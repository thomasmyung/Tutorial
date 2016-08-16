from adb_android import adb_android

def screenshot(image_name):
	adb_android('shell screencap /sdcard/%s' %(image_name))