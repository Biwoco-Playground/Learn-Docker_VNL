
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print(' '.join(parts))
print(','.join(parts))

h = 'Vu'
l = 'Long'
n = 'Ngoc'

print(h,n,l,sep=' ')
print('+'.join(sample()))