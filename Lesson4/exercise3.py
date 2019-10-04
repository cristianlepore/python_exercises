def mult(a, b):
    '''
    input: two numbers
    output: a recursion of a times b
    '''
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

a = 10
b = 5

print(mult(a, b))
