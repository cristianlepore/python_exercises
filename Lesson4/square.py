def square(x):
    '''
    This function takes in one number and returns one number.
    '''
    return x**2

x = int(input("Insert a number:"))

num = square(x)

print("The square of the number",end=' ')
print(x, end=' ')
print("is", end=' ')
print(num)