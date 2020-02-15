#!/usr/bin/python

def changeme( mylist ):
	mylist = [1,2,3,4];
	print "Values inside the function: ", mylist
	return

mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
