#!/usr/bin/python

import os,sys,stat

fd = os.open("/tmp/foo.txt",os.O_RDONLY)

os.fchown(fd,100,-1)

os.fchown(fd,-1,50)

print "Changed ownership successfully!"

os.close(fd)
