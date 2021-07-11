from itertools import islice,dropwhile
a = ['a','b','c','d',1,2,3,4,5]
for x in islice(a,3,None):
    print(x)
print('-----'*25)
for x in dropwhile(lambda x : x!='a',a):
    print(x)