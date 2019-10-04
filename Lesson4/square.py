'''
@author: cristianlepore
'''

def square(x):
    '''
    input: a number
    output: a number. The square of the input
    '''
    return x**2

x = int(input("Insert a number:"))

num = square(x)

print("The square of the number",end=' ')
print(x, end=' ')
print("is", end=' ')
print(num)