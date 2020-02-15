#!/usr/bin/python

str = "this is\tstring example...wow!!!";

print "Original string: " +str;
print "Default exapnded tab: " +str.expandtabs();
print "Double expanded tab: " + str.expandtabs(16);
