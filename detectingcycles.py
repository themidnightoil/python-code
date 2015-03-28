import sys
import collections

txt = open('detectingcycles','r')

for numbers in txt:
	array = []
	numbers = numbers.strip().split()
	numbers = [int(x)  for x in numbers]
	count = collections.Counter(numbers)
	

	for x in numbers:
		if count[x] > 1:
			if x not in array:
				array.append(x)
	for x in array:
		print x,
	print ''

