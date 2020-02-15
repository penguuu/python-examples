#!/usr/bin/python

import os, sys, stat

# Set a file execute by the group
os.chmod("foo.txt", stat.S_IXGRP)

# Set a file write by others.
os.chmod("foo.txt",stat.S_IWOTH)

print "Changed mode successfully!"

