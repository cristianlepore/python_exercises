# -*- coding: utf-8 -*-
"""
@author: cristianlepore
"""

low = 0
high = 100
ans = ''
print("Please think of a number between", end=' ')
print(str(low), "and", end=' ')
print(str(high) + "!")

while ans != 'c':
    x = round( (high + low) / 2 )
    print("Is your secret number", str(x) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    ans = input()

    if ans != 'l' and ans != 'h' and ans != 'c':
        print("Sorry, I did not understand your input.")

    if ans == 'l':
        low = x
    elif ans == 'h':
        high = x