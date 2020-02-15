#!/usr/bin/python

import os,sys

statinfo = os.stat("foo7.txt")

print statinfo

statinfo = os.stat_float_times()

print statinfo
