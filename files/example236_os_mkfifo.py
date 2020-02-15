#!/usr/bin/python

import os, sys

path = "/tmp/hourly"

os.mkfifo(path,0644)

print "Path is created"
