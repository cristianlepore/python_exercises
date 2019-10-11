'''
@author: cristianlepore
'''

class Person(object):
    def __init__(self, x, y):
        self.height = x
        self.weight = y 
    

height = 1.77
weight = 80

p = Person(height, weight)

print("Person height:", end=' ')
print(p.height, "m")
print("Person weight:", end=' ')
print(p.weight, "Kg")
