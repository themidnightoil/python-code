
import sys

txt = open('rollercoaster', 'r')


for line in txt:
	line = line.strip()
	array = []
	caps = True
	for letter in line:
		array.append(letter.upper()) if letter.isalpha()  and caps else array.append(letter)
		caps = not caps if letter.isalpha() else caps

	print ''.join(array)



