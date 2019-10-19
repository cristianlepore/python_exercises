'''
@author: cristianlepore
'''

def longest(s):
    '''
    input: a str s in alphabetical order.
    output: a str. A substring of s.
    Return the longest substring of s in alphabetical order.
    '''

    def less(str):
        '''
        input: a str of two characters.
        returns True if the first char is less or equal to the second char, otherwise returns False.
        '''
        return str[0] <= str[1]

    tmp = ''
    output = ''
    for i in range(len(s)-1):
        if less(s[i:i+2]):
            tmp += s[i]
        else:
            if len(output) < len(tmp):
                output = tmp + s[i]
                tmp = ''
            else:
                tmp = ''

    if len(output) < len(tmp):
        output = tmp + s[i+1]
    
    return output


# My string in alphabetical order
s = 'azcbobobegghakl'
s = s.lower()
print(longest(s))
