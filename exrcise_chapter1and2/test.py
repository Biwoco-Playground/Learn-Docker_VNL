# from underthesea import word_tokenize

# sentence = 'Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò'
# k =  'Chợ thịt chó nổi tiếng ở Sài Gòn bị truy quét'
# k = k.lower()
# data = word_tokenize(sentence, format="text")

# print(data)

from nltk import word_tokenize

data = 'I read the some thng about the regular expression but still some confusion so please suggest any link or code overview for the same.'

print(word_tokenize(data))