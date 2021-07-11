import re


"""
    function load file text
"""
def load_file_text(file):
    data = ''
    with open(file,'r+',encoding='utf8') as f :
        data = f.read()
    return data

"""
    function load file stopwrod
    return list stopword
"""
def load_stopword(file):
    stop_word = []
    with open(file,'r+',encoding='utf8') as f:
        while True:
            data = f.readline()
            if data == '':
                break
            data = data.split()
            stop_word.append(data.pop())
    return stop_word

#split sentences in a paragraph
def split_sentences(text):
    regEx = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
    sentences = regEx.split(text)
    return sentences

#create regex stop word
def regex_stopword(file_stopword):
    list_stopword = load_stopword(file_stopword)
    regex = []
    for word in list_stopword:
        word_regex =  r'\b' + word + r'(?![\w-])' 
        regex.append(word_regex)
    result_regex_stopword = re.compile('|'.join(regex))
    return result_regex_stopword

def pre_processing(sentences,stopword):
    result = []
    for k in sentences:
        temp = re.sub(stopword, '|',k)
        results_temp = temp.split('|')
        for result_temp in results_temp:
            result_temp = str(result_temp).strip().lower()
            result_temp = re.sub(',','',result_temp)
            if result_temp != '':
                result.append(result_temp)
    return result

def word_separation(text,min_word):
    result = []
    regex = re.compile('[^a-zA-Z0-9_\\+\\/]')
    for single in regex.split(text):
        k = single.strip().lower()
        if len(k) > min_word and k != '' :
            result.append(k)
    return result

def calculate_word(pre_processing):
    frequency = {}
    degree = {}
    for phrase in pre_processing:
        word_list = word_separation(phrase,0)
        word_list_degree = len(word_list) - 1
        for word in word_list:
            frequency.setdefault(word,0)
            frequency[word] += 1
            degree.setdefault(word,0)
            degree[word] += word_list_degree
    
    for item in frequency:
        degree[item] = frequency[item] + degree[item]
    
    word_score = {}
    for item in frequency:
        word_score.setdefault(item,0)
        word_score[item] = degree[item] / frequency[item]
    
    return word_score

def sum_point(pre_processing,word_score):
    result = {}
    for phrase in pre_processing:
        result.setdefault(phrase,0)
        word_list = word_separation(phrase,0)
        k = 0
        for word in word_list:
            k += word_score[word]
        result[phrase] = k
    return result

def Rake(text,file_stop_word):
    regex = regex_stopword(file_stop_word)
    pre = pre_processing(split_sentences(text),regex)
    calculate = calculate_word(pre)
    sumP = sum_point(pre,calculate)
    result = sorted(sumP.items(),key= lambda x : x[1],reverse=True)
    return result

file = 'stopword.txt'

text = "Last, but not least, be aware that there are subtle issues that can arise in filename handling related to encodings. Normally, the entries returned by a function such as os.list dir() are decoded according to the system default filename encoding. However, it’s possible under certain circumstances to encounter un-decodable filenames. Recipes 5.14 and 5.15 have more details about handling such names."
hhh = 'Elon Musk has shared a photo of the spacesuit designed by SpaceX. This is the second image shared of the new design and the first to feature the spacesuit’s full-body look.'
ahihi = 'Keyword extraction is not that difficult after all. There are many libraries that can help you with keyword extraction. Rapid automatic keyword extraction is one of those.'

a = load_file_text('file.txt')
print(Rake(a,file))
print('-------'*24)
print(load_file_text('file.txt'))
# k = regex_stopword(file)
# a = pre_processing(split_sentences(ahihi),k)

# for i in split_sentences(ahihi):
#     print(i)

# print('-------'*24)

# print(a)

# print('-------'*24)

# x = calculate_word(a)

# print(x)

# print('-------'*24)

# z = sum_point(a,x)
# l = sorted(z.items(),key= lambda x : x[1],reverse=True)
# print(z)
# print('-------'*24)
# print(l)
