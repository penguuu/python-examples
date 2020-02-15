#!/usr/bin/python

fo = open("foo.txt","wb")
print "Name of the file: ",fo.name

fid = fo.fileno()
print "File Descriptor: ",fid

fo.close()
