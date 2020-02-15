#!/usr/bin/python

fo = open("example196_file_readlines.py","r")
print "Name of the file: ", fo.name

line = fo.readlines()
print "Read Line: %s" % line

line = fo.readlines(2)
print "Read Line: %s" % line

fo.close()
