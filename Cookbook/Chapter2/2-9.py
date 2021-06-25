import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

t1 = unicodedata.normalize('NFD',s1)
t11= ''.join(c for c in t1 if not unicodedata.combining(c))

print(t1)
print(t11)
print('--'*25)

t2 = unicodedata.normalize('NFC',s2)
t12= ''.join(c for c in t2 if not unicodedata.combining(c))

print(t2)
print(t12)