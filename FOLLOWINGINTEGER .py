import sys
from itertools import product, chain ,permutations

txt = open('followinginteger','r')

array=[]
for number in txt:
	for x in permutations(number):
		print x

