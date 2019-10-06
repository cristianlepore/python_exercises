# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/var/www/html/exercises/Lesson6/Problem1/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in lettersGuessed:
      if letter in secretWord:
        secretWord = secretWord.replace(letter, '')

    if len(secretWord) == 0:
      return True
    else:
      return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    resultingWord = ''
    for char in secretWord:
      if char in lettersGuessed:
        resultingWord += char
      else:
        resultingWord += '_ '

    return resultingWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = string.ascii_lowercase
    for char in letters:
      if char in lettersGuessed:
        letters = letters.replace(char, '')
    
    return letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    '''
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")
    lettersGuessed = []

    '''
    * Ask the user to supply one guess (i.e. letter) per round.
    '''
    availableLetters = getAvailableLetters(lettersGuessed)
    numGuesses = 8

    while(numGuesses > 0 and not isWordGuessed(secretWord, lettersGuessed)):
      print("You have", numGuesses, "guesses left.")
      print("Available letters:", end=' ')
      print(availableLetters)
      let = input("Please guess a letter: ")
      lettersGuessed.extend(let)

      '''
      * The user should receive feedback immediately after each guess 
        about whether their guess appears in the computers word.
      '''
      if let not in availableLetters:
        print("The letter has already been chosen!")
        print(getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
      elif let in secretWord:
        '''
        * After each round, you should also display to the user the 
          partially guessed word so far, as well as letters that the 
          user has not yet guessed.
        '''
        print("Good guess:", end = ' ')
        print(getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        availableLetters = getAvailableLetters(lettersGuessed)
      else:
        print("Oops! That letter is not in my word:", end = ' ')
        print(getGuessedWord(secretWord, lettersGuessed))
        print("-------------")
        availableLetters = availableLetters.replace(let, '')
        numGuesses -= 1

    if isWordGuessed(secretWord, lettersGuessed):
      print("Congratulations, you won!")
    else:
      print("Sorry, you ran out of guesses. The word was", end = ' ')
      print(secretWord + ".")

    '''
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print("Welcome to the game Hangman!")
hangman(secretWord)
