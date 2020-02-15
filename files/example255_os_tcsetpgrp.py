#!/usr/bin/python

import os,sys

print "Current working dir :%s" % os.getcwd()

fd = os.open("/dev/tty",os.O_RDONLY)
f = os.tcgetpgrp(fd)

print "The process group associated is: "
print f

os.tcsetpgrp(fd,2672)
print "done"

os.close(fd)
print "Closed the file successfully!"
