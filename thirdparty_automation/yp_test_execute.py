import os
import time
import sys
import subprocess
import yp_test
import threading
import screen_record
import random
from adb_android import adb_android

def execute_test1(yp):
	for x in range(0,5):
		yp.yp_launch_app()
		time.sleep(random.uniform(.5,5))
		yp.yp_close_app()

	

