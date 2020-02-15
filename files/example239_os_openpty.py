#!/usr/bin/python

import os

m,s = os.openpty()

print m
print s

s = os.ttyname(s)
print m
print s
