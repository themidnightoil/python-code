import sys
import collections

txt = open('selfdescribingnumbers', 'r')

for number in txt:
	shit= True
	count = [(int(x),y) for x, y in collections.Counter(number.strip()).iteritems() if int(y) and int(x) != 0]
	enum = [(x,int(y)) for x, y in list(enumerate(number.strip())) if int(y) and int(x) != 0]

	for x in enum:
		if x not in count:
			shit = False


	if shit == False:
		print 0
	else: print 1



