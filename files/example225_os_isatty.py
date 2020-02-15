#!/usr/bin/python

import os,sys

fd = os.open("foo10.txt", os.O_RDWR|os.O_CREAT)

os.write(fd,"This is test")

ret = os.isatty(fd)

print "Returned value is: ", ret

os.close(fd)
