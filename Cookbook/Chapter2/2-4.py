import re
from sys import path
datept = re.compile(r'\d+/\d+/\d+')
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if datept.match(text1) :
    print('yes')
else:
    print('no')

print('-'*20)

if datept.match(text2):
    print('yes')
else:
    print('no')

print('-'*20)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datept.findall(text))

print('-'*20)

t = '30/03/2000'
t1 = '30/03/2000aasdasdsad'
datept1 = re.compile(r'(\d+)/(\d+)/(\d+)$')
datept2 = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datept2.match(t1))