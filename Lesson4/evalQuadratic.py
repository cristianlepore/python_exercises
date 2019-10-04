'''
@author: cristianlepore
'''

def evalQuadratic(a, b, c, x):
    '''
    input: four numbers
    output: return a polynomial expression
    '''
    return a*x**2 + b*x + c

a = 2
b = 3
c = 5
x = 2

print(evalQuadratic(a, b, c, x))
