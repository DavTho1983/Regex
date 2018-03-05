import re

def multi_re_find(patterns, phrase) :

    for pat in patterns :
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd..dsds...dssssss...sddddd'

test_pattern1 = ['sd*'] #an s followed by 0 or more d-s
test_pattern2 = ['sd+'] #an s followed by 1 or more d-s
test_pattern3 = ['sd?'] #an s followed by 0 or 1 d-s
test_pattern4 = ['sd{3}'] #an s followed by 3 d-s
test_pattern5 = ['sd{1,3}'] #an s followed by 1 or 3 d-s
test_pattern6 = ['s[sd]+'] #an s followed by 1 or more s-s or 1 or more d-s (any pattern that starts with an s)

multi_re_find(test_pattern6, test_phrase)
