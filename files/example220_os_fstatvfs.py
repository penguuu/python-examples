#!/usr/bin/python

import os, sys

fd = os.open("foo6.txt", os.O_RDWR|os.O_CREAT)

info = os.fstatvfs(fd)

print "File Info: ", info

print "Maximum filename length: %d" % info.f_namemax
print "Free blocks: %d" % info.f_bfree

os.close(fd)
