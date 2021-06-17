
a = int(input('You must enter an integer greater than 100 and less than 999 : '))
if a > 99 and a < 999:
	print('reversed numer is {}{}{}'.format(a % 10, (a // 10)%10, a//100))
else:
	print('Syntax error')
