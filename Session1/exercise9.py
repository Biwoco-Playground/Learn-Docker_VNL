import math

print('Enter the lengths of 3 sides a,b and c of a triangle')
a = int(inpu1t('a = '))
b = int(input('b = '))
c = int(input('c = '))

cv = a + b + c
p = cv / 2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print('Chu vi :', cv,'\nDien tich :',s)
