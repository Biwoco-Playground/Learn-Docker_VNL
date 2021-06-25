
def pri_all_char():
    x = True
    k = ord('A')
    while x == True :
        if k == ord('Z'):
            x = False
        print(chr(k))
        k += 1
        

pri_all_char()