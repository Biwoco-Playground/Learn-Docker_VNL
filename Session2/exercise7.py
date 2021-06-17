def check_day(x,k):
    month = {
        1 : 31,
        2 : 28 + k,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    return month.get(x)

def check_dmy(d,m,y):

    if y > 0 and 0 < m < 13 :
        if y % 4 == 0 and y % 100 == 0 or y % 400 == 0 :
            k=1
        else:
            k=0

        if d <= check_day(m,k) :
            print('Yes')
        else:
            print('No')
    else:
        print('No')


print('Enter day month year ')
d = int(input('day : '))
m = int(input('Month : '))
y = int(input('Year : '))
check_dmy(d,m,y)

# print(check_day(2,1))