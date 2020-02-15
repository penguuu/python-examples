#!/usr/bin/python

import os,sys

stinfo = os.stat("foo7.txt")
print stinfo

print "access time of foo7.txt: %s" % stinfo.st_atime
print "modified time of foo7.txt: %s" % stinfo.st_mtime

os.utime("foo7.txt",(1330712280,1330712292))
print "done!"
