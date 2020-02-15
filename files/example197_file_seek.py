#!/usr/bin/python

fo = open("example197_file_seek.py","r")
print "Name of the file: ", fo.name

line = fo.readline()
print "Read Line: %s" % line

fo.seek(0,0)
line = fo.readline()
print "Read Line: %s" % line

fo.close()
