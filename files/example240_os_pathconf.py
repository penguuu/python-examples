#!/usr/bin/python

import os, sys

print "%s" % os.pathconf_names

no = os.pathconf('example240_os_pathconf.py', 'PC_NAME_MAX')
print "Maximum length of a filename :%d" % no

no = os.pathconf('example240_os_pathconf.py', 'PC_FILESIZEBITS')
print "file size in bits: %d" % no
