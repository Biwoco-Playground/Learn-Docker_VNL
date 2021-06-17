
def check(ch):
    global a,b
    toan = {
        '+' : 'a + b = ' + str(a + b),
        '-' : 'a - b = ' + str(a - b),
        '*' : 'a * b = ' + str(a * b),
        '/' : 'a / b = ' + str(a / b)
    }
    print(toan.get(ch))
print('Nhap so a, b va ky tu ch')
a = int(input('a = '))
b = int(input('b = '))
ch = input('ch = ')

check(ch)