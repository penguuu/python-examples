#!/usr/bin/python

import os
import stat

filename = "foo15.txt"

mode = 0600|stat.S_IRUSR

os.mknod(filename,mode);
