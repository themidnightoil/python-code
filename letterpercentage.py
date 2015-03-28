import sys

txt = open('letterpercentage','r')



for line in txt:
	line= line.strip()
	lower = 0.00
	upper =0.00
	line = list(line)
	total = len(line)
	for letter in line:
		if letter.islower():
			lower +=1
	upper = total-lower
	if lower != 0:
		lower =100/(total/lower)
	if upper != 0:
		upper = 100/(total/upper)
	print 'lowercase: %0.2f uppercase: %0.2f' % (lower,upper )




