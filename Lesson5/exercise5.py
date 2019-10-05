'''
@author: cristianlepore
'''

def applyToEach(L, f):
    '''
    input: a list and a function
    output: A list after having applied the function f to each element of the list
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def mult(a):
    '''
    input: one numbers
    output: one number. The multiplication of a times 5
    '''
    return a * 5

def add(a):
    '''
    input: one numbers
    output: one number. Add +1 to the element a
    '''
    return a + 1

def square(a):
    '''
    input: one numbers
    output: one number. The power of a
    '''
    return a**2


testList = [1, -4, 8, -9]

'''
# Applied function
print(applyToEach(testList, mult))

# Add +1 to each element
print(applyToEach(testList, add))
'''

# Square of each element
print(applyToEach(testList, square))
