#!/usr/bin/python

import os,sys

fd = os.open("foo7.txt",os.O_RDWR)

ret = os.read(fd,12)
print ret

os.close(fd)
print "Closed the file successfully!"
