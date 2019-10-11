'''
#author: cristianlepore
'''

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newAge):
        self.age = newAge
    def set_name(self, newName = None):
        self.name = newName
    def __str__(self):
        return "animal:" + str(self.name) + "," + str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + "," + str(self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:" + str(self.name) + "," + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_frineds(self, fName):
        if fName not in self.friends:
            self.friends.append(fName)
    def speak(self):
        print("hello")
    def age_difference(self, other):
        diff = abs(self.age - other.age)
        if self.age > other.age:
            if diff == 1:
                print(self.name, "is", diff, "year older than", other.name)
            else:
                print(self.name, "is", diff, "years older than", other.name)
        else:
            if diff == 1:
                print(self.name, "is", diff, "year older than", other.name)
            else:
                print(self.name, "is", diff, "years younger than", other.name)
    def __str__(self):
        return "person:" + str(self.name) + "," + str(self.age)

class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def __Str__(self):
        return "student:" + str(self.name) + "," + str(self.age)

myCat = Cat(2)
myCat.set_name('Miky')
myAnimal = Animal(1)
myAnimal.set_name = 'Foo'

myRabbit = Rabbit(5)

eric = Person("Eric", 45)
john = Person("John", 32)

eric.speak()
eric.age_difference(john)
Person.age_difference(john, eric)