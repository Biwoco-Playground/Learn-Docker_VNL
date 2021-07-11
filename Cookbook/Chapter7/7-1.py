import html

def make_element(name,value,**attrs):
    keyvays = [' %s="%s"'%item for item in attrs.items()]
    attr_str = ''.join(keyvays)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name =name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

def avg(first,*rest):
    return (first + sum(rest))/(1 + len(rest))

def test(*t,**k):
    for i in t:
        print(k)
    print(i)

print(avg(1,2,3,4))
print(make_element('p','Vu Ngoc Long',size='large'))
print('---'*25)
print(test(1,2,3,4,'a','d','f','v'))