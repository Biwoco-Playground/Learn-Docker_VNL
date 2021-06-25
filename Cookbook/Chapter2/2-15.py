s = '{name} has {n} messages.'
a = s.format(name='Long',n='Dep')

print(a)
x = 'Name= {t} , Year = {y}'
t = 'Vu Ngoc Long'
y = 2000
k = x.format_map(vars())
print(k)