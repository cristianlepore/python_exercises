'''
@author: cristianlepore
'''

def iterPower(base, exp):
    '''
    input: int or float.
    output: compute the base times itself exp times
    '''
    result = 1
    for i in range(exp):
        result *= base
    return result

base = 3
exp = 5
print(iterPower(base, exp))
