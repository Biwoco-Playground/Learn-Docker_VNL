a = ['a','b','c']
from itertools import permutations

for x in permutations(a):
    print(x)

for x in permutations(a,2):
    print(x)