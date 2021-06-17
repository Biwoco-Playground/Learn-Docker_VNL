max = 0
def number_max(a,b,c):
    global max
    max = a
    if b > a :
        max = b
    if c > a :
        max = c
    return max

print('You must enter 3 integers :')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print('The largest of three numbers a,b and c is',number_max(a,b,c))
