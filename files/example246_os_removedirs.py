#!/usr/bin/python

import os, sys

print "The dir is: %s" % os.listdir(os.getcwd())

os.removedirs("/tutorialsdir")

print "The dir after removal is: " % os.listdir(os.getcwd())
