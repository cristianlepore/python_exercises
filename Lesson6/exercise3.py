def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    values = aDict.values()
    for words in values:
        if len(words) > 1:
            for i in range(len(words)):
                count += 1
        else:
            count += 1
    return count

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
