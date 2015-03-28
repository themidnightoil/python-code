import sys
from itertools import product

txt = open('stringlist','r')


for line in txt:
	num , letters = line.split(',')
	num = int(num)
	letters = list(letters.strip())
	array=[]

	print ','.join(''.join(x) for x in sorted(set(product(letters, repeat=num)))),
	print '\n',