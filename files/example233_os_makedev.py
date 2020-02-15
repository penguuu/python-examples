#!/usr/bin/python 

import os, sys

path = "foo7.txt"

info = os.lstat(path)

major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print "Major Device Number :", major_dnum
print "Minot Device Number :", minor_dnum

dev_num = os.makedev(major_dnum, minor_dnum)
print "Device Number : ", dev_num
