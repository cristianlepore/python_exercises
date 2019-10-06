'''
@author: cristianlepore
'''

def longestSubstr(s):
    '''
    input: a string
    output: the longest substring
    '''
    substr = ''
    max = 0
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            substr += s[i]
            max += 1
        else:
            substr += s[i]
            result = substr
            substr = ''

    # Returned value
    return result

s = "abcbcd"
print(longestSubstr(s))
