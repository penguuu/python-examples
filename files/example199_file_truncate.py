#!/usr/bin/python

fo = open("foo.txt","rw+")
print "Name of the file: ", fo.name

line = fo.readline()
print "Read Line: %s" % line

fo.truncate()

line = fo.readline()
print "Read Line: %s" % line

fo.close()
