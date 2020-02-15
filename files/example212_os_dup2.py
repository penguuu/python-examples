#!/usr/bin/python

import os,sys

# Open file
fd = os.open("foo5.txt",os.O_RDWR|os.O_CREAT)

# Write one string
os.write(fd,"This is is text")

# Duplicate this file descriptor as 1000
fd2 = 1000
os.dup2(fd,fd2);

# Now read this file from the beginning using fd2
os.lseek(fd2,0,0)
str = os.read(fd2,100)
print "Read String is: ",str

os.close(fd)
