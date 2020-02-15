#!/usr/bin/python

import os,sys,stat

# Open file /tmp/foo.txt
fd = os.open("/tmp/foo.txt", os.O_RDONLY)

# Set a file execute by the group
os.fchmod(fd,stat.S_IXGRP)

# Set a file write by others.
os.fchmod(fd,stat.S_IWOTH)

print "Changed mode successfully!"

os.close(fd)
