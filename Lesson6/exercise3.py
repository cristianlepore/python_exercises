'''
@author: cristianlepore
'''

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: a number that returns the number of values in the dictionary.
    '''
    count = 0
    values = aDict.values()
    print(values)
    for words in values:
        if len(words) > 1:
            for i in words:
                count += 1
        else:
            count += 1
    return count

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
