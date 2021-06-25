import requests

def fillter_a(a):
    fir_a = 0
    end_a = 0
    out = '<'
    n = []
    for i in a:
        if i == '<' and fir_a != 2:
            fir_a +=1
            continue
        if i != 'a'and fir_a == 1 :
            fir_a -=1
            continue
        if i == 'a'and fir_a != 2 :
            fir_a += 1
        if i == '<' and fir_a == 2 and end_a == 0:
            end_a += 1
        elif i == '/' and fir_a == 2 and end_a == 1:
            end_a +=1
        elif i != '/' and fir_a == 2 and end_a == 1:
            end_a = 0
        elif i != 'a' and fir_a == 2 and end_a == 2:
            end_a = 0
        elif i == 'a' and fir_a == 2 and end_a == 2:
            end_a += 1
        elif i != '>' and fir_a == 2 and end_a == 3:
            end_a = 0
        elif i == '>' and fir_a == 2 and end_a == 3:
            end_a += 1
        if fir_a == 2:
            out = out + i
        if fir_a == 2 and end_a == 4:
            n.append(out)
            out = '<'
            fir_a=0
            end_a=0
    return n

def conent_a(a):
    item = 0
    z = []
    for i in a:
        for j in i:
            if j == 'h' and item == 0:
                item += 1
            elif j != 't' and item ==1:
                item =0
            elif j == 't' and item ==1:
                item +=1
            elif j == 't' and item ==2:
                item +=1
            elif j != 'p' and item == 3:
                item=0
            elif j == 'p' and item == 3:
                item += 1
            elif j != 's' and item == 4:
                item=0
            elif j == 's' and item == 4:
                item += 1
        if item == 5:
            z.append(i)
            item = 0
    return z

def get_content(a):
    content =''
    check =0
    for i in a:
        if i == '>' and check == 0:
            check += 1
            continue
        elif i == '<' and check ==1:
            check +=1
        if check == 1:
            content = content + i
        if check == 2:
            break
    return content

def get_links(s):
    content =''
    t = 0
    for i in s:
        if i == '"' and t == 0:
            t += 1
            continue
        elif i == '"' and t == 1:
            t += 1
        if t == 1:
            content = content + i
        if t == 2:
            break
    return content

def get_content_tag(a):
    sta_tag = 0
    end_tag = 0
    check = 2
    content = '<tabl'
    for i in a:
        #check tag <table>
        if i == '<' and sta_tag == 0:
            sta_tag += 1
        elif i != 't' and sta_tag == 1:
            sta_tag = 0
        elif i == 't' and sta_tag == 1:
            sta_tag += 1
        elif i != 'a' and sta_tag == 2:
            sta_tag = 0
        elif i == 'a' and sta_tag == 2:
            sta_tag += 1
        elif i != 'b' and sta_tag == 3:
            sta_tag = 0    
        elif i == 'b' and sta_tag == 3:
            sta_tag += 1
        elif i != 'l' and sta_tag == 4:
            sta_tag = 0    
        elif i == 'l' and sta_tag == 4:
            sta_tag += 1
        elif i != 'e' and sta_tag == 5:
            sta_tag = 0    
        elif i == 'e' and sta_tag == 5:
            sta_tag += 1
        elif check >= 1 and sta_tag == 6:
            sta_tag = 0
            check -= 1
            continue
        #check tag </table>
        if i == '<' and sta_tag == 6 and end_tag == 0 and check ==0:
            end_tag += 1
        elif i != '/' and sta_tag == 6 and end_tag == 1 and check ==0:
            end_tag = 0
        elif i == '/' and sta_tag == 6 and end_tag == 1 and check ==0:
            end_tag += 1
        elif i != 't' and sta_tag == 6 and end_tag == 2 and check ==0:
            end_tag = 0
        elif i == 't' and sta_tag == 6 and end_tag == 2 and check ==0:
            end_tag += 1
        elif i != 'a' and sta_tag == 6 and end_tag == 3 and check ==0:
            end_tag = 0
        elif i == 'a' and sta_tag == 6 and end_tag == 3 and check ==0:
            sta_tag += 1
        elif i != 'b' and sta_tag == 6 and end_tag == 4 and check ==0:
            end_tag = 0    
        elif i == 'b' and sta_tag == 6 and end_tag == 4 and check ==0:
            end_tag += 1
        elif i != 'l' and sta_tag == 6 and end_tag == 5 and check ==0:
            end_tag = 0    
        elif i == 'l' and sta_tag == 6 and end_tag == 5 and check ==0:
            end_tag += 1
        elif i != 'e' and sta_tag == 6 and end_tag == 6 and check ==0:
            end_tag = 0    
        elif i == 'e' and sta_tag == 6 and end_tag == 6 and check ==0:
            end_tag += 1
        elif i == '>' and sta_tag == 6 and end_tag == 7 and check ==0:
            end_tag +=1
        if sta_tag == 6 and check ==0:
            content = content + i
        elif end_tag == 8:
            break
    return content

def pr_a(k):
    a = []
    for i in k:
        d = {}
        d['title']= get_content(i)
        d['links'] = get_links(i)
        a.append(d)
    return a
if __name__ == '__main__':                
    reponse = requests.get('https://news.ycombinator.com').content
    a = get_content_tag(reponse.decode('utf-8').strip())
    c = conent_a(fillter_a(a)) 
    k = pr_a(c)
    for i in k:
        print(i)