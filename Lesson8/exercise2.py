'''
@author: cristianlepore
'''

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again.")

print("Outside")
