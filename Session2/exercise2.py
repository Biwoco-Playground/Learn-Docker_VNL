a = int(input('You enter month in year : '))

if ( 0 < a < 13):
    if(a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12):
        print('The month have 31 days')
    elif a == 2:
        print('The month have 28 or 29 days')
    else:
        print('The month have 30 days')

else:
    print('not month')