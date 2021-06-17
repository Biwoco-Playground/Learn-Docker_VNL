import math

def equation2(a,b,c):
    denta = (b ** 2) - 4*a*c
    if denta >= 0:
        
        if denta != 0:
            x1 = (-b + math.sqrt(denta)) / (2*a)
            x2 = (-b - math.sqrt(denta)) / (2*a)
            print('x1 =', x1, '\nx2 =',x2)
        else:
            print('x =',round(-b/(2*a)))
    else:
        print('Equation has no solution')


print('quadratic equation 2 : ax^2 + bx + c = 0 ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

equation2(a,b,c)

