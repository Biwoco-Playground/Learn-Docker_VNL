import math
def area_perimeter(a,b,c):
    if(a + b > c and a + c > b and b +c > a):
        cv = a + b + c
        p = cv / 2
        dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print ('Area :',round(dt,2), '\nPerimeter :',cv)
    else:
        print('Do not from a triangle')

print('Enter length of the 3 size')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
area_perimeter(a,b,c)