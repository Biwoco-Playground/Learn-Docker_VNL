from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello\n')
    f.write('Vu Ngoc Long')

    f.seek(0)
    print(f.read())