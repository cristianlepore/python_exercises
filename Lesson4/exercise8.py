'''
@author: cristianlepore
'''

def gcdRecur(a, b):
    '''
    input: two numbers
    output: the gcd between a and b
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(17, 12))
