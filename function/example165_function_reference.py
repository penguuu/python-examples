#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
	"This changes a passed list into this function"
	mylist.append([1,2,3,4]);
	print "Values inside the function: ", mylist
	return

# Call the changeme funtion
mylist = [10,20,30];
changeme( mylist );
print "Value outside the function: ", mylist
