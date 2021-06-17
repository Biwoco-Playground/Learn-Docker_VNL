
def menu(a,b,x):
    switch = {
        1: a + b,
        2: a - b
    }
    return switch.get(x)

print(menu(3,2,1))
