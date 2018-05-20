#!/usr/bin/python

import psutil
import datetime
import sys
import os
for x in sys.argv:
	try:
		n=int(x)
		p=psutil.Process(n)
		pp=psutil.Process(p.ppid())
		print "Process ID : " , p.pid
		print "Process name : " , p.name()
		print "Process Status : " , p.status()
		print "Process Parent id : " ,p.ppid()
		print "Process Parent name :",pp.name()
		d=p.create_time()
		print "Process Creation Time : " , datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
		print "Files opened by the process : " ,p.open_files()
		print "Memory info : " , p.memory_info().rss
		print "-------------------------------------------"	
	except Exception as ex:
		print ex
	
