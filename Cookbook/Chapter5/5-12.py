import os

path = '/home/long/Long/Python/Session1/Learn-Docker_VNL/Cookbook/Chapter5/5-11.py'

print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir('/hom/long/'))
print(os.path.islink('/usr/bin/python3'))
print(os.path.realpath('/usr/bin/python3'))