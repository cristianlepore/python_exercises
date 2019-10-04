'''
@author: cristianlepore
'''

def isIn(char, aStr):
    '''
    input: a char and a string in alphabetical ordering
    output: True if a char is in aStr, False otherwise
    '''
    if len(aStr) == 1 and char == aStr[0]:
        return True
    else:
        middle = len(aStr) // 2

    if middle == 0 :
        return False
    elif char == aStr[middle]:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle])
    elif char > aStr[middle]:
        return isIn(char, aStr[middle+1:])
 

a = 'u'
aStr = 'abcefilnprstvz'
print(isIn(a, aStr))
