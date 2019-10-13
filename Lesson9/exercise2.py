'''
@author: cristianlepore
'''

class Person(object):

    def __init__(self, x, y):
        self.height = x
        self.weight = y

    def height_difference(self, other):
        height_diff = self.height - other.height
        return height_diff

    def weight_difference(self, other):
        weight_diff = self.weight - other.weight
        return weight_diff

    def __str__(self):
        return "< Height:" + str(self.height) + " m, Weight: " + str(self.weight) + " Kg >"

p1 = Person(1.77, 70)
p2 = Person(1.65, 80)
print(str(round(p2.height_difference(p1), 2) * 100) + " cm")
print(str(round(p2.weight_difference(p1), 2)) + " Kg")
print(p1)
print(p2)
print(isinstance(p1, Person))
