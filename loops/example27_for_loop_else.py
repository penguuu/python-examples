#!/usr/bin/python

for num in range(10,20):	# to iterate 10 to 20
	for i in range(2,num):	# to iterate on the factors of the number
		if num%i == 0:
			j=num/i
			print '%d equals %d * %d' % (num,i,j)
			break # to move to the next number, the #first FOR
	else:
		print num,'is a prime number'
