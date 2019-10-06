'''
@author: cristianlepore
'''

def recurPower(base, exp):
    '''
    input: two numbers.
    output: one number. The base times itself exp times.
    '''
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

base = 10
exp = 5
print(recurPower(base, exp))
