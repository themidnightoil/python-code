import sys


prime=[]
notprime=[]
txt = open('primenumbers','r')
for number in txt:
	array =[]
	for i in range (2, int(number)):
		if i in prime:
			print i
			break
		else:
			for x in range(2,i):
				if i%x ==0:
					break
			else: 
				array.append(str(i))
				prime.append(str(i))
	print prime
	print ','.join(array),
	print'\n',





