def odd(num):
    '''
    input: a number
    output: True if the number is odd. False otherwise
    '''

    return num % 2 > 0

x = int(input("Insert a number: "))
if(odd(x)):
    print("The number ", x, " is odd")
else:
    print("The number ", x, " is even")
