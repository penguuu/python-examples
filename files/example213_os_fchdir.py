#!/usr/bin/python

import os,sys

# Change directory to /home/pengu
os.chdir("/home/pengu")

# Print current working directory
print "Current working dir : %s" % os.getcwd()

# open directory /tmp

fd = os.open("/tmp", os.O_RDONLY)

# use os.fchdir() method to change the dir
os.fchdir(fd)

# Print current working directory
print "Current working dir: %s" % os.getcwd()

os.close(fd)

