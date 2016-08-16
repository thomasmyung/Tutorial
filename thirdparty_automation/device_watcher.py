import os
import sys
import subprocess
from adb_android import adb_android
import datetime

def get_deviceid():

	adb_device_output_raw = adb_android.devices()
	adb_device_output = adb_device_output_raw[1]

	device_count = len(adb_device_output.split('\n'))-3


	deviceid_list =[]
	output_list = adb_device_output.split()

	deviceid_list.append(output_list[4])
	const = 6
	for y in range (0,device_count-1):
		deviceid_list.append(output_list[const])
		const += 2
	return deviceid_list

def get_device_model(deviceid):
	current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
	f = open('E:\Automation2\list_of_available_device.txt','w')
	f.write("this txt file is updated every 10 sec.\nBelow device list is last updated %s\n\n" %(current_time))
	f.close()
	for x in range (0, len(deviceid)):
		cmd = 'adb -s %s shell getprop ro.product.model' %(deviceid[x])
		devicemodel =  subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
		line = devicemodel.communicate()
		line_str = str(line)
		end = line_str.find('\r\r\n') -13
		start = line_str.find("'")+1

		#create txt file with list of connected devices
		f = open('E:\Automation2\list_of_available_device.txt','a')
		f.write(line_str[start:end])
		f.close



