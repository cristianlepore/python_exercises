'''
@author: cristianlepore
'''

count = 0
strToFind = "bob"
s = "azcbobobegghakl"

while(strToFind in s):
    s = s[s.find(strToFind) + 1 : -1]
    count += 1
print(count)