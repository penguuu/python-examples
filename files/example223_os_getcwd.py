#!/usr/bin/python

import os,sys

os.chdir("/usr/bin")

print "Current working dir : %s" % os.getcwd()

fd = os.open("/tmp",os.O_RDONLY)

os.fchdir(fd)

print "Current working dir: %s" % os.getcwd()

os.close(fd)
