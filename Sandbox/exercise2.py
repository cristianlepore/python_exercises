'''
@author: cristianlepore
'''

def occurrences(s, str):
    '''
    input: s. The string to check
    input: str. The sentence to check
    output: an integer. The number of times str occurs in s.
    '''
    l = len(str)
    num = 0
    try:
        assert len(s) >= l, 'The string must be longer than s.'
    except:
        return 0
    else:
        for i in range(len(s)-(l-1)):
            if str == s[i:i+l]:
                num += 1
        return num

s = 'azcbobobegghakl'
s = s.lower()
str ='bob'
print(occurrences(s, str))
