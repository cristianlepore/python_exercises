'''
@author: cristianlepore
'''

from exercise2 import MITPerson

class Student(MITPerson):
    pass

class UG(Student):

    def __init__(self, name, classYear = None):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, "yo bro, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(Obj):
    return isinstance(Obj, Student)
