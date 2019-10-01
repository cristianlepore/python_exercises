def countChars(mySentence):
    '''
    input: a string
    output: an int. The number of vowels into the string
    '''

    def toLower(x):
        '''
        input: a string
        putput: a string. It puts the input string into lower case.
        '''
        return x.lower()

    # Assignment
    vowels = 0
    notVowels = 0
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    # Convert string to lower case
    mySentence = toLower(mySentence)

    # For loop
    for i in mySentence:
        if i in vowelsList:
            vowels += 1
        else:
            notVowels += 1
    # Value to return
    return (vowels, notVowels)

# My sentence
mySentence = input("Insert a sentence: ")
(vowels, notVowels) = countChars(mySentence)
print("The number of vowel in the sentence is:", end=' ')
print(vowels)
print("The number of the remainng lecters is:", end=' ')
print(notVowels)
