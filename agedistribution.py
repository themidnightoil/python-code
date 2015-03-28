import sys
txt = open('agedistribution','r')

for number in txt:
	number =int(number)
	if 0<= number <= 2:
		print 'Still in Mama\'s arms' 
	elif 3 <= number <= 4:
		 print'Preschool Maniac' 
	elif 5 <= number <= 11:
		print 'Elementary school'
	elif 12 <= number <= 14:
		print'Middle school' 
	elif 15 <= number <= 18:
		print 'High school' 
	elif 19 <= number <= 22:
		print 'College'
	elif 23 <= number <= 65:
		print 'Working for the man' 
	elif 66 <= number <= 100:
		print 'The Golden Years'
	elif 100 < number < 0 :
		print "This program is for humans"
	