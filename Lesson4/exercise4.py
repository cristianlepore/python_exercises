'''
@author: cristianlepore
'''

def factorial(x):
    '''
    input: a number
    output: the factorial of x
    '''

    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

x = 4
print(factorial(x))