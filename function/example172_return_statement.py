#!/usr/bin/python

def sum(arg1,arg2):
	total = arg1 + arg2;
	print "Inside the function : ", total
	return total;

total = sum(10,20);
print "Outside the function : ", total
