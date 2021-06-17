def check(ch):
    if 'A' <= ch <= 'Z' :
        print('Chu Hoa')
    elif 'a' <= ch <= 'z':
        print('chu thuong')
    elif '0' <= ch <= '9' :
        print('So')
    else:
        print('Ky tu khac')

ch = input('Nhap 1 ky tu : ')
check(ch)