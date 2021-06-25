import math

def SPoint(K):
    Name,*point= K
    avg = sum(point) / len(point)
    return avg
    #yield Name,a,point

a = ['Vu Ngoc Long',9,8,8,7]
Name,*M = a
print('Name :',Name,SPoint(a))
print('--'*25)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print('--'*25)
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
z = line.split(':')
print(z)

print('--'*25)
items = [10, 10, 7, 4, 5, 9]
def sum(a):
    head,*tail = a
    return head + sum(tail) if tail else head

print(sum(items))
print('--'*25)

def s():
    yield 5
    yield 6

print(next(z) for z in s()) 

