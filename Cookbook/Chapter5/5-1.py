with open('test.txt','wt') as f:
    a = input('Enter :')
    f.write(a)
    f.close()

with open('test.txt','rt') as f:
    date = f.read()
    print(date)
    f.close()

with open('test.txt','rt',newline='',encoding='utf-8') as f:
    date = f.read()
    print(date)