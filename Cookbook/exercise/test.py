import re
from typing import Text

def word_separation(text,min_word):
    result = []
    regex = re.compile('[^a-zA-Z0-9_\\+\\/]')
    for single in regex.split(text):
        k = single.strip().lower()
        if len(k) > min_word and k != '' :
            result.append(k)
    return result

# a = 'Vu Ngoc Long, Vu Ngoc Kieu Vy'
# r = re.compile(r'\b' + 'Ngoc' + r'(?![\w-])')
# print(r.split(a))

a = 'Vu Ngoc Long'
k = word_separation(a,0)
print(k)