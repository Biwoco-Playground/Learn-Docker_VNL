time = int(input('You must enter minutes :'))
i = 0
while time >= 60:
	i += 1
	time -= 60
print('', i, 'h {}'.format(time))

