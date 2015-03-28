
import re
import sys

with open('validparenthesis', 'r') as input:
    test_cases = input.read().strip().splitlines()
    stuff =	re.compile(r'\[\]|\{\}|\(\)')



for test in test_cases:
	print test
	while True:

		if len(stuff.findall( test)):
			print len(stuff.findall( test))
			print stuff.findall( test)
			print True
			break
		if not len(re.findall(stuff, test)):
			print len(stuff.findall( test))
			print False
			break