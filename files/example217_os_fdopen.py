#!/usr/bin/python

import os,sys

fd = os.open("foo6.txt",os.O_RDWR|os.O_CREAT)

fo = os.fdopen(fd,"w+")

print "Current I/O pointer position: %d" % fo.tell()

fo.write("Python is a great language.\nYeah its great!!\n");

os.lseek(fd,0,0)
str = os.read(fd,100)
print "Read String is : ", str

print "Current I/O pointer position :%d" % fo.tell()

fo.close()

print "Closed the file successfully!"
