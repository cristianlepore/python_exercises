'''
@author: cristianlepore
'''

def countVowels(s):
    '''
    input: a string.
    output: an integer. Count the number of vowels in the sentence s.
    '''
    vowels = 'aeiou'
    num = 0
    for char in s:
        if char in vowels:
            num += 1
    
    return num

s = 'azcbobobegghakl'
s = s.lower()
print("Number of vowels:", end=' ')
print(countVowels(s))
