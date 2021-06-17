import os

def check_divisible_3(ch):
    a = int(ch[0]) + int(ch[1]) + int(ch[2])
    if a % 3 == 0:
        print('divisible by 3') 
    else:
        print('Not')

i = True
while i == True :
    ch = input('Enter Charater : ')
    # print('---------',len(ch))
    if int(len(ch)) == 3 :
        check_divisible_3(ch)
        i = False
    else:
        # os.system('cls')
        print('Retype')

