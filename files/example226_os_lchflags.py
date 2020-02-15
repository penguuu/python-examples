#!/usr/bin/python

import os,sys

path = "foo8.txt"
fd = os.open(path, os.O_RDWR|os.O_CREAT)

os.close(fd)

ret = os.lchflags(path,os.UF_IMMUTABLE)

print "Changed file flag successfully!"
