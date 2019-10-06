'''
@author: cristianlepore
'''

def applyEachTo(L, x):
    '''
    input: a list and a number
    output: a list with appended the value x
    '''
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a * a

def halve(a):
    return a / 2

def inc(a):
    return a + 1

print(applyEachTo([inc, square, halve, abs], -3))
