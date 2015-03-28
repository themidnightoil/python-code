import sys
from collections import Counter


txt = open('rightmostchar','r')


for line in txt:
	phrase ,char  = line.split(',')
	char = char.strip()
	phrase2 = list(phrase.strip())
	phrase = list(enumerate(phrase.strip()))
	for x,y in phrase[::-1]:
		if y == char:
			print x
			break
		if char not in phrase2:
			print -1
			break
			
