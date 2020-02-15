#!/usr/bin/python

import os

tmpfile = os.tmpfile()
tmpfile.write('Temporary newfile is here...')
tmpfile.seek(0)

print tmpfile.read()
tmpfile.close
