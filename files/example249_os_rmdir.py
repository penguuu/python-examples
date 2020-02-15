#!/usr/bin/python

import os,sys

print "the dir is: %s" % os.listdir(os.getcwd())

os.rmdir("mydir")

print "the dir is:" % os.listdir(os.getcwd())
