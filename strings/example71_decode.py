#!/usr/bin/python

str = "this is string example...wow!!!";
str = str.encode('base64', 'strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')
