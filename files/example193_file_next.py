#!/usr/bin/python

fo = open("example193_file_next.py","r")
print "Name of the file: ", fo.name

for index in range(10):
	line = fo.next()
	print "Line No %d - %s" % (index,line)

fo.close()
