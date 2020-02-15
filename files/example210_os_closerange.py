#!/usr/bin/python

import os, sys

fd = os.open("foo.txt4", os.O_RDWR|os.O_CREAT)

os.write(fd,"This is test")

os.closerange(fd,fd)

print "Closed the file successfully!!"
