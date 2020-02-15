#!/usr/bin/python

fo = open("foo.txt","wb")
print "Name of the file: ",fo.name

ret = fo.isatty()
print "Return value : ", ret

fo.close()
