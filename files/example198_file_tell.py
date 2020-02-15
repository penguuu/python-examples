#!/usr/bin/python

fo = open("example198_file_tell.py","r")
print "Name of the file: ", fo.name

line = fo.readline()
print "Read Line: %s" % line

pos = fo.tell()
print "Current Position: %d" % pos

fo.close()
