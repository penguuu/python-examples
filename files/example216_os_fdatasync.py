#!/usr/bin/python

import os,sys

fd = os.open("foo6.txt", os.O_RDWR|os.O_CREAT)

os.write(fd,"This is test")

os.fdatasync(fd)

os.lseek(fd,0,0)
str = os.read(fd,100)
print "Read String is : ", str

os.close(fd)

print "Closed the file successfully!"
