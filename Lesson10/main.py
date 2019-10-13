'''
@author: cristialepore
'''

from exercise1 import Person
from exercise2 import MITPerson
from exercise3 import Student
from exercise3 import UG
from exercise3 import Grad
from exercise3 import TransferStudent
from exercise4 import Professor

alex = UG('alex Righetti', 2017)
cristian = UG('Cristian Lepore', 2018)
daniele = UG('Daniele Negri', 2019)
alberto = MITPerson('Alberto Angela')
andrea = Professor('Andrea Visconti', 'Informatica')

print(andrea.lecture("Hi there"))
