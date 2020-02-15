#!/usr/bin/python

dict1 = {'Name': 'Zara', 'Age' : 7};
dict2 = {'Name': 'Mahnaz', 'Age' : 27};
dict3 = {'Name': 'Abid', 'Age' : 27};
dict4 = {'Name': 'Zara', 'Age': 7};

print "Return Value : %d " % cmp(dict1,dict2)
print "Return Value : %d " % cmp(dict2,dict3)
print "Return Value : %d " % cmp(dict1,dict4)
