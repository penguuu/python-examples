#!/usr/bin/python

def temp_convert(var):
	try:
		return int(var)
	except ValueError, Argument:
		print "The argument does not contain numbers\n", Argument

temp_convert("xyz")
