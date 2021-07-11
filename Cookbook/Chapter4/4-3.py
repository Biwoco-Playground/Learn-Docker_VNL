def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment

for i in frange(0,5,0.25):
    print(i)

print(sum(frange(0,5,0.25)))
print(list(frange(0,5,0.25)))