#!/usr/bin/python

import os, sys

print "The dir is: %s" % os.listdir(os.getcwd())

os.rename("tutorialsdir","tutorialsdirectory")

print "Successfully renamed."

print "the dir is: %s" % os.listdir(os.getcwd())
