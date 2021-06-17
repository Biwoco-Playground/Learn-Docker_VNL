def check(ch):
    if ch in('a','e','o','i','u'):
        print('vowels')
    else:
        print('consonants')

ch = input('You must enter charater : ')
check(ch.lower())