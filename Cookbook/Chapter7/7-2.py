def mininum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(mininum(1,2,3,4,5,6,clip=0))