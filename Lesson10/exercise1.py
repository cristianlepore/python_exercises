'''
@author: cristianlepore
'''

import datetime

class Person(object):
    
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    
    def getLastName(self):
        return self.lastName
    
    def __str__(self):
        return self.name
    
    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        try:
            if self.birthday != None:
                return (datetime.date.today - self.birthday).days
        except TypeError:
            print('Fail')

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.lastName < other.lastName
        else:
            return self.lastName < other.lastName
