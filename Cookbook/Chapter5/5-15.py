def bad_filename(filename):
    return repr(filename)[1:-1]

filename = 'b\udce4d.txt'
try:
    print(filename)
    print('aaa')
except UnicodeEncodeError:
    print(bad_filename(filename))

print(filename)