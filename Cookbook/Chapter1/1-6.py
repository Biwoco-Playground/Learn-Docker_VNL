from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print('--'*25)
print(d['a'])

print(dict(d))

a = {i: i + 10 for i in range(10)}

print(a)