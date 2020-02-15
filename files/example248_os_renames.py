#!/usr/bin/python

import os,sys

print "Current directory is: %s" % os.getcwd()

print "The dir is: %s" % os.listdir(os.getcwd())

os.renames("foo10.txt","tutorialsdirectory/foo10.txt")

print "Successfully renamed."

print "The dir is: %s" % os.listdir(os.getcwd())
