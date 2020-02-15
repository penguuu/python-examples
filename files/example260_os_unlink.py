#!/usr/bin/python

import os,sys

print "The dir is: %s" % os.listdir(os.getcwd())

os.unlink("foo10.txt")

print "The dir after removal of path : %s" % os.listdir(os.getcwd())
