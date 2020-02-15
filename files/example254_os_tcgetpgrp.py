#!/usr/bin/python

import os,sys

print "Current working dir: %s" % os.getcwd()

fd = os.open("/dev/tty",os.O_RDONLY)
f = os.tcgetpgrp(fd)

print "the process group associated is: "
print f

os.close(fd)
print "closed the file successfully"
