#!/usr/bin/python

import os, sys

# Open a file
fd = os.open("foo.txt4", os.O_RDWR|os.O_CREAT)

os.write(fd,"This is test")

os.close(fd)

print "Closed the file succesfully!"
