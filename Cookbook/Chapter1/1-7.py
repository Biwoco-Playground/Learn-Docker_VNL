from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
b = {}
b['a'] = 1
b['b'] = 2
b['c'] = 3
b['d'] = 4
print('OrderedDict\n')
for key,values in d.items():
    print(key,values)
print('--'*25)
print('Dict\n')

for key,values in b.items():
    print(key,values)
