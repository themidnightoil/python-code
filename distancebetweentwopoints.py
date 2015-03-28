import sys
import math

txt = open('distancebetweentwopoints', 'r')

for digits in txt:
	digits = digits.strip().replace(')','').replace('(','').replace(',','').split(' ')
	x1 ,y1 ,x2 ,y2 = map(int, digits)

	z = ((x2 - x1)**2)+((y2 - y1)**2)
	print int(math.sqrt(z))




