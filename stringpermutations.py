import sys
from itertools import permutations

txt = open('stringpermutations','r')


for line in txt:
	line =list(line.strip())
	length =len(line)
	print ','.join(sorted(set(''.join(x) for x in permutations(line,length))))
	

