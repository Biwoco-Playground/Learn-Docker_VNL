with open('test.txt') as f:
    try:
        while True:
            line = next(f)
            if line is None:
                break
            print(line, end='')
    except StopIteration:
        pass