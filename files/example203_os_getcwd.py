#!/usr/bin/python

import os

path = "/tmp"

retval = os.getcwd()
print "Current working directory %s" % retval

os.chdir(path)

retval = os.getcwd()
print "Directory changed successfully %s " % retval
