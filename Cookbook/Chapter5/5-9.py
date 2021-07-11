import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin','wb') as f:
    f.write(b'Hello Wrold')

buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'Hallo'
buf = memoryview(buf)   
buf2 = buf[-5:]
buf2[:] = b'LongL' 
print(str(buf))

with open('sample.bin','wb') as f:
    f.write(buf)