#!/usr/bin/python

import os,sys

ret = os.access("foo.txt",os.F_OK)
print "F_OK - return value %s" % ret

ret = os.access("foo.txt",os.R_OK)
print "R_OK - return value %s" % ret

ret = os.access("foo.txt",os.W_OK)
print "W_OK - return value %s" % ret

ret = os.access("foo.txt",os.X_OK)
print "X_OK - return value %s" % ret
