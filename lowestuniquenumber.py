import sys
from collections import Counter
txt = open('lowestuniquenumber','r')

for numbers in txt:
	array=[]
	num = numbers.split()
	
	numbers = Counter(numbers.split())
	for x,y in numbers.iteritems():
		if y == 1:
			array.append(x)
	try:
		print num.index(array[0])+1
	except:
		print 0

