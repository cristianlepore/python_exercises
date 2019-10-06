'''
@author: cristianlepore
'''

def fourthPower(x):
    '''
    input: a number
    output: a number. The fourth power of x
    '''
    return square(square(x))

def square(x):
    '''
    input: a number
    output: a number. The square of the input number using the Newton-Raphson theorem.
    '''
    guess = x/2
    while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))
    return guess

epsilon = 0.01
numGuesses = 0
x = int(input("Enter a number: "))
guess = round(fourthPower(x), 4)
print("The fourth power of ", x, " is ", guess)
