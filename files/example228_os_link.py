#!/usr/bin/python

import os,sys

path = "foo7.txt"

fd = os.open(path, os.O_RDWR|os.O_CREAT)

os.close(fd)

dst = "foo11.txt"
os.link(path,dst)

print "Created hard link successfully!"
