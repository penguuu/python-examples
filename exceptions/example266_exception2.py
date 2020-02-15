#!/usr/bin/python

try:
	fh = open("testifile","w")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print "Error: can\'t find file or read data"
else:
	print "written content in the file successfully"
