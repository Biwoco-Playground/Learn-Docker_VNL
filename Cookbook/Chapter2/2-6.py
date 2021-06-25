import re

text = 'UPPER PYTHON, lower python, Mixed Python'
a = re.findall('python',text,flags=re.IGNORECASE)
b = re.sub('python','Long',text,flags=re.IGNORECASE)

print(text)
print(a)
print(b)