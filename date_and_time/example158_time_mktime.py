#!/usr/bin/python

import time

t = (2009,2,17,17,3,38,1,48,0)

secs = time.mktime(t)
print "time.mktime(t) : %f" % secs
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))
