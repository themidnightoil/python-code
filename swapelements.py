import sys


txt = open('swapelements' , 'r')


for line in txt :
	
	numbers ,pos= line.strip().split(':')
	numbers = numbers.split()
	pos = [x.split('-') for x in pos.replace(' ','').replace(',',' ').split()]
	for k,v in pos:
		numbers[int(k)],numbers[int(v)] = numbers[int(v)],numbers[int(k)] 
	for x in numbers: print x,
	print '\n',