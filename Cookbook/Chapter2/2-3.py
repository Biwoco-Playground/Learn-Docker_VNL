from fnmatch import fnmatchcase

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]

a = [addr for addr in addresses if fnmatchcase(addr,'* ST')]
b = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]

print(a)
print(b)
