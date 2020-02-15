#!/usr/bin/python

import os

path = "foo.txt"

flags = os.SF_NOUNLINK 
retval = os.chflags(path,flags)
print "Return Value: %s" % retval
