#!/usr/bin/python

str = "this is string example... wow!!!";

suffix = "wow!!!";

print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";

print str.endswith(suffix,2,4);
print str.endswith(suffix,2,6);
