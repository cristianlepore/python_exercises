def oddTuples(aTup):
    '''
    input: a tuple.
    output: a new tuple containing only the odd element of the input tuple
    '''
    # Start code here
    
    # Definition of the new tuple
    myTuple = ()

    # Loop
    for i in range(len(aTup)):
        if i % 2 == 0:
            myTuple += (aTup[i],)
    # Return value
    return myTuple

# Definition of my tuple
aTup = ('I', 'am', 'a', 'test', 'tuple')

# Call the procedure
print(oddTuples(aTup))
