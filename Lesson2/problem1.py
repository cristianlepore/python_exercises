'''
@author: cristianlepore
'''

vowels = 0
s = "string of character"

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1

print(vowels)