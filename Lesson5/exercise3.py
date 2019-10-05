'''
@author: cristianlepore
'''

def oddTuples(aTup):
    '''
    input: a tuple
    output: a tuple with only the odds elements
    '''
    return aTup[::2]

# Definition of my tuple
aTup = ('I', 'am', 'a', 'test', 'tuple')

# Call the procedure
print(oddTuples(aTup))
