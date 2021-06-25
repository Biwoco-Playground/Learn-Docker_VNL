def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe1(items, key=None):
        seen = set()
        for item in items:
            #val = item if key is None else key(item)
            if key is None:
                val = item
            else:
                val = key(item)
            if val not in seen:
                yield item
                seen.add(val)
z = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
a = [1, 5, 2, 1, 9, 1, 5, 10]
b =list(dedupe(a))
print(a,'\n',set(a),'\n',b)
print('--'*25)
k = list(dedupe1(a, key=lambda d: (d['x'],d['y'])))
print(z,'\n')
print(k)