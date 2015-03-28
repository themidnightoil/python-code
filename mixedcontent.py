import sys
import re

txt = open('mixedcontent','r')

for line in txt:
    if test:
        shit = ','.join(re.findall('[a-z]+', line))
        shut = ','.join(re.findall('\d+', line))
        separator = '|' if (shit and shut) else ''
        print separator.join((shit, shut))