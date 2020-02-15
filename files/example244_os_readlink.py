#!/usr/bin/python

import os

src = '/usr/bin/python'
dst = '/tmp/python'

os.symlink(src,dst)

path = os.readlink(dst)
print path
