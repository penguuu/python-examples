#!/usr/bin/python

import os,sys

print "Current working dir: %s" % os.getcwd()

fd = os.open("/dev/tty",os.O_RDONLY)

p = os.ttyname(fd)
print "the terminal device associated is: "
print p
print "done!!"

os.close(fd)
print "closed the file successfully!"
