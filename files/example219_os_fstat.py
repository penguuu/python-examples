#!/usr/bin/python

import os, sys

fd = os.open("foo6.txt", os.O_RDWR|os.O_CREAT)

info = os.fstat(fd)

print "File Info : ", info

print "UID of the file :%d" % info.st_uid
print "GID of the file :%d" % info.st_gid

os.close(fd)
