import sys
import collections
import re


txt = open('beautifulstring', 'r')
for line in txt:
	line= ''.join([let for let in line if let.isalpha() ])
	alphaToken = 26
	total = 0
	line = line.lower().strip()
	line=collections.Counter(line)
	line = line.values()
	for x in reversed(sorted(line)):
		total += x * alphaToken
		alphaToken -=1
			
	print total

		
