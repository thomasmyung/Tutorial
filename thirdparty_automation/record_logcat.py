import os
import sys
import subprocess


class LogStorage(object):
	def __init__(self):
		super(LogStorage, self).__init__()
		self.log = []
	def record(self, *args):
		for args in args:
			print (args)
		d= args[0]
		print d
		proc = subprocess.Popen(d, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		while True:
			line = proc.stdout.readline()
			print line
			line_str =  str(line)
			if line != '':
				self.log.append(line_str.rstrip() + '\n')
			else:
				break
	def getEvents(self):
		#a = open('test.txt','r')
		#print (a.read)
		return(self.log)
	def clearLog(self):
		self.log = []


