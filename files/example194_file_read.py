#!/usr/bin/python

fo = open("example194_file_read.py","r")

print "Name of the file: ",fo.name

line = fo.read(10)
print "Read Line: %s" % (line)

fo.close()
