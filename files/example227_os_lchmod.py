#!/usr/bin/python

import os, sys

path = "foo8.txt"

fd = os.open(path, os.O_RDWR|os.O_CREAT)

os.close(fd)

os.lchmod(path,stat.S_IXGRP)

os.lchmod("foo7.txt",sat.S_IWOTH)

print "Changed mode successfully!"
