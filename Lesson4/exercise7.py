'''
@author: cristianlepore
'''

def gcdIter(a, b):
    '''
    input: two numbers
    output: the greates common divisor between a and b
    '''
    if a >= b:
        start = b
    elif a < b:
        start = a

    div = start
    while(div >= 0):
        if a % div == 0 and b % div == 0:
            return div
        elif div == 0:
            return div
        div -= 1

print(gcdIter(17, 12))
