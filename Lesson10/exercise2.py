'''
@author: cristianlepore
'''

from exercise1 import Person

class MITPerson(Person):
    nextIdNum = 1

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.name + " says: " + utterance)
