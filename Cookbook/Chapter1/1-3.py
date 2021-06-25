from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

a = [1,2,3,4,5]
for line, prevlines in search(a, 'python', 5):
    for pline in prevlines:
        print(pline, end='')
    print(line, end='')
    print('-'*20)