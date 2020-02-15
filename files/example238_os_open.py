#!/usr/bin/python

import os,sys

fd = os.open("foo17.txt", os.O_RDWR|os.O_CREAT)

os.write(fd,"This is test")
os.close(fd)

print "Closed the file successfully!"
