import sys
import re
txt = open('json','r')





for line in txt:
	pattern = re.compile( r'Label (\d+)')
	d= [int(x) for x in pattern.findall(line)]
	print sum(d)