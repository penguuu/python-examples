#!/usr/bin/python

import os,sys

fd = os.open("foo20.txt",os.O_RDWR|os.O_CREAT)

ret = os.write(fd,"test text")

print "the number of bytes written: "
print ret

print "written successfully"

os.close(fd)
print "closed the file successfully"
