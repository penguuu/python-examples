#!/usr/bin/python

import os,sys

path = "/usr/bin/"

dirs = os.listdir(path)

for file in dirs:
	print file
