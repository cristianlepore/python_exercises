'''
#author: cristianlepore
'''

class Animal(object):
    def __init__(self, age, name = None):
        self.age = age
        self.name = name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newAge):
        self.age = newAge
    def set_name(self, newName = None):
        self.name = newName
    def __str__(self):
        return "animal:" + str(self.name) + ",", str(self.age)

myAnimal1 = Animal(2)
myAnimal2 = Animal(3, 'Mike')
