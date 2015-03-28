import sys

txt = open('minimumcoins','r')

for x in txt :
	x = int(x)
	array =[]
	array.append(x/5)
	x = x - 5*array[0]
	array.append(x/3)
	x = x - 3*array[1]
	array.append(x/1)
	x = x - 1*array[2]
	print sum(array)






