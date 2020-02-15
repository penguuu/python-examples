#!/usr/bin/python

import os, sys

fd = os.open("foo6.txt", os.O_RDWR|os.O_CREAT)

print "%s" % os.pathconf_names

no = os.fpathconf(fd, 'PC_LINK_MAX')
print "Maximum number of links to the file. :%d" % no

no = os.fpathconf(fd,'PC_NAME_MAX')
print "Maximum length of a filename: %d" % no

os.close(fd)

print "Closed the file successfully!!"
