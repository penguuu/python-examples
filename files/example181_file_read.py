#!/usr/bin/python

fo = open("foo.txt","r+")
str = fo.read(10);
print "Read String is : ", str
fo.close()
