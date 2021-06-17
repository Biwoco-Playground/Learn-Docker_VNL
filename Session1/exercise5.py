import math

a = float(input('a = '))
x = float(input('x = '))

if x > 0 and a > 0 and a != 1 :
	print('log_a(x) =', math.log(x)/math.log(a) )
else:
	print('You must enter x > 0, a >0 và a \# 1')
