'''
@author: cristianlepore
'''

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me one number: "))
    print(a/b)
except ValueError:
    print("Bug in user input.")
except ZeroDivisionError:
    print("Divisiont by zero not allowed.")
except TypeError:
    print("Type error.")
else:
    print("Okay. No error found.")
finally:
    print("Procedure completed!")

myList = [10, 20, 30]
print(myList.index(11))

try:
    A = 2
    print(3*a)
except NameError:
    print("Name error.")
