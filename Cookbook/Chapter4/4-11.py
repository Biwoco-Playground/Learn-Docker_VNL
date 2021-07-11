from itertools import zip_longest

a = [1,5,2,3,4,6,7]
b = ['c','a','b','d','a','f']
for x,y in zip(a,b):
    print(x,y)
for x in zip(b,a):
    print(x)
for x in zip_longest(b,a,fillvalue=0):
    print(x)
