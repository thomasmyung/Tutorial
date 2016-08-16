import threading
import os
import sys
import subprocess
from adb_android import adb_android

def screenrecord(record_time, testcase):
	print 'code reached'
	adb_android.shell('screenrecord --bit-rate 6000000 --time-limit %s /sdcard/%s' %(record_time, testcase))