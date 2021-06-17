
def equation(a,b):
    if(a == 0):
        if b == 0 :
            print('Equation infinite solutions')
        else:
            print('Equation has no solution')
    else:
        print('x =',round(-b/a,2))

print('Frist degree equation ax + b = 0')
a = int(input('a = '))
b = int(input('b = '))
equation(a,b)