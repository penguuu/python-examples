#!/usr/bin/python

import os, sys

path = "foo7.txt"

info = os.lstat(path)

major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print "Major device number : ", major_dnum
print "Minor device number : ", minor_dnum
