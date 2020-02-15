#!/usr/bin/python

import os,sys

print "The dir is: %s" % os.listdir(os.getcwd())

os.remove("foo15.txt")

print "The dir after removal of path : %s" % os.listdir(os.getcwd())
