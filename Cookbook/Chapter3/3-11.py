import random as rd
a = [1,2,3,4,5,6]
print(a)
print(rd.choice(a))
print(rd.sample(a,3))
rd.shuffle(a)
print(a)