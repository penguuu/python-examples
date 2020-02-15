#!/usr/bin/python

import os, sys

fd = os.open("foo.txt4",os.O_RDWR|os.O_CREAT)

d_fd = os.dup(fd)

os.write(d_fd,"This is test")

os.closerange(fd,d_fd)

print "Closed all the files successfully!"
