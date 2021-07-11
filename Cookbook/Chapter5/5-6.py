import io
s = io.StringIO()
s.write('Vu Ngoc Long\n')
print('Ahihi Do Ngoc',file=s)
print(s. getvalue())
print(s.read(4))

k = io.BytesIO()
k.write(b'Vu Ngoc Long')
print(k.getvalue())