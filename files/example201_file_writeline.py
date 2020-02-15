#!/usr/bin/python

fo = open("foo2.txt","rw+")
print "Name of the file: ", fo.name

seq = ["This is 6th line\n", "This is 7th line"]
fo.seek(0,2)
line = fo.writelines(seq)

fo.seek(0,0)
for index in range(7):
	line = fo.next()
	print "Line No %d - %s" % (index,line)

fo.close()
