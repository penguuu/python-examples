#!/usr/bin/python

import os, sys

os.chown("foo.txt",0,-1)

print "Changed ownership successfully!"
