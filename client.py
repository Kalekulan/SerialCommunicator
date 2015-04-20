#!/usr/bin/python2.7

#14424562,0,1,0

import cPickle
import os
import sys, getopt, serial



def main(argv):
   sender = ''
   unit = ''
   state = ''
   dim = ''

   try:
      opts, args = getopt.getopt(argv,"s:u:t:d:",["sender=","unit=","state=","dim="])
   except getopt.GetoptError:
      print "getopt error"
      print 'client.py -s <sender> -u <unit> -t <state> -d <dim>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'client.py -s <sender> -u <unit> -t <state> -d <dim>'
         sys.exit()
      elif opt in ("-s", "--sender"):
         sender = arg
      elif opt in ("-u", "--unit"):
         unit = arg
      elif opt in ("-t", "--state"):
         state = arg
      elif opt in ("-d", "--dim"):
         dim = arg
   print 'Sender ID:', sender
   print 'Unit ID:', unit
   print 'State:', state
   print 'Dimlevel:', dim

   #communicate with another process through named pipe
   #one for receive command, the other for send command

   wfPath = "/usr/local/sbin/sFifo"
   #rfPath = "./p2"
   wp = open(wfPath, 'w')
   string = sender + "," + unit + "," + state + "," + dim + "\n"
   wp.write(string)		
   wp.close()

		 

if __name__ == "__main__":
   main(sys.argv[1:])
