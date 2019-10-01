def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    def toChars(aStr):
        aStr = aStr.lower()
        ans = ''
        for c in aStr:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    aStr = toChars(aStr)
    # Start of my code
    middle = len(aStr) // 2
    if middle == 0:
        return False
    elif char == aStr[middle]:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle])
    elif char > aStr[middle]:
        return isIn(char, aStr[middle+1:])
    

char = 'g'
char = char.lower()
aStr = "abdghilmnrstvz"

print(isIn(char, aStr))