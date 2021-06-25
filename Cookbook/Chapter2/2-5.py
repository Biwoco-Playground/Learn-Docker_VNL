import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

a = re.sub(r'(\d+)/(\d+)/(\d+)$',r'\3-\1-\2',text)

print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))