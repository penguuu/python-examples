#!/usr/bin/python

import os,sys

os.chdir("/usr/bin")

print "Current working dir : %s" % os.getcwdu()

fd = os.open("/tmp", os.O_RDONLY)

os.fchdir(fd)

print "Current working dir: %s" % os.getcwdu()

os.close(fd)
