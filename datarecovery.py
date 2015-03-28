import sys


text = open('datarecovery','r')

for line in text:
	dictionary={}
	line, numbers = line.split(';')
	line = line.split()
	numbers =[int(x)-1for x in numbers.split()]
	zipper =zip(numbers,line)
	zipper= sorted(zipper)
	for x , y in zipper:
		print y,


