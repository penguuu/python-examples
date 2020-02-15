#!/usr/bin/python

import os, sys

path = "foo7.txt"
fd = os.open(path, os.O_RDWR|os.O_CREAT)

os.close(fd)

info = os.lstat(path)

print "File info: ", info

print "UID of the file :%d" % info.st_uid
print "GID of the file :%d" % info.st_gid
