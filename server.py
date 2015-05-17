#!/usr/bin/python2.7

import cPickle
import os
import serial
import time
import select
import sys



#communicate with another process through named pipe
#one for receive command, the other for send command
rfPath = "/usr/local/sbin/sFifo"
#wfPath = "./p2"
#wfPath = "./p1"

READ_ONLY = select.POLLIN | select.POLLPRI

PIDFILE = "/run/serialService.pid"

try:
    ser = serial.Serial("/dev/ttyUSB0")#, baudrate=9600)#, timeout= 3.0)
	
except serial.SerialException:
	print 'Port already open or not found'
	sys.exit()
	
print 'Serial port opened.'

try:
#    os.mkfifo(wfPath)
    os.mkfifo(rfPath)
except OSError:
    pass

pw = open(PIDFILE, 'w')
pw.write(str(os.getpid()))
pw.close()

rp = open(rfPath, 'r+')
#rp = os.open(rfPath, os.O_RDWR)
print rp
poller = select.poll()
#print poller
poller.register(rp)#READ_ONLY)
#print poller

while True:
	
	[(filedesc, event)] = poller.poll()
	# event = poller.poll()
	# print 
	# if len(event) > 0: flag = event[1]
	# fd = event[0]
	# for fd, flag in event:
		# i = 0
		# Retrieve the actual socket from its file descriptor
		# print "filedesc = ", fd
		# print "event = ", flag
		# time.sleep(5)
		
	# print select.POLLIN
	# print select.POLLPRI
	# print select.POLLOUT
	# print select.POLLERR
	# print select.POLLHUP
	# print select.POLLNVAL
	# print event
	# print filedesc
	
	# time.sleep(1)
	# print event
	# time.sleep(0.5)
	if event <= 7:
#	if (event & select.POLLIN) or (event & select.POLLPRI):
	#print event
	#if event > 0:
#	if (filedesc is rp) & (event & select.POLLIN):

#	if event & (select.POLLIN | select.POLLPRI):
#	if flag & select.POLLIN:
		#print "read"
		try:
			data = rp.readline()
			#print "hej"
			if len(data) > 0:
				print "P2 hear: %s" % data
				#rp.close()
				ser.write(data)
				#rp.seek(0)
				#rp.truncate()
				#wp = open(wfPath, 'w') #erases content
				#wp.close()
				#rp.open()
			#else:
				#rp.close()
				#time.sleep(0.005)
		except IOError as e: 
			print "I/O error({0}): {1}".format(e.errno, e.strerror)

		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise


rp.close()
os.unlink(rfPath)


#wp = open(wfPath, 'w')
#wp.write("P2: I'm fine, thank you! And you?")		
#wp.close()
#rp = open(rfPath, 'r')
#response = rp.read()
#print "P2 hear %s" % response
#rp.close()
