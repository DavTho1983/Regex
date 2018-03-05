import re

def multi_re_find(patterns, phrase) :

    for pat in patterns :
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase1 = 'This is a string! But it has punctuation. How can we remove it?'
test_phrase2 = 'This is a string with numbers 12312 and a symbol #hashtag'



test_pattern1 = ['[^!.?]+'] #strip of specified punctuation
test_pattern2 = ['[a-z]+'] #return sequences of lowercase chars
test_pattern3 = ['[A-Z]+'] #return sequences of uppercase chars
test_pattern4 = [r'\d+'] #return sequence of digits
test_pattern5 = [r'\D+'] #return sequence of nondigits
test_pattern6 = [r'\s+'] #return sequence of whitespace
test_pattern7 = [r'\S+'] #return sequence of non-whitespace
test_pattern8 = [r'\w+'] #return sequence of alphanumeric chars
test_pattern9 = [r'\W+'] #return sequence of non-alphanumeric chars



multi_re_find(test_pattern9, test_phrase2)
