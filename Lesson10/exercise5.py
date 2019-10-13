'''
@author: cristianlepore
'''

class Grades(object):
    
    def __init__(self):
        self.students = []
        self.grades = []
        self.isSorted = True

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
