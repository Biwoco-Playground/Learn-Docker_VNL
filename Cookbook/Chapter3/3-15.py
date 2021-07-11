from datetime import datetime

text = '2000-03-30'
d = datetime.strptime(text,'%Y-%m-%d')
print(d)

