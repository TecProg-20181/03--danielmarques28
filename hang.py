import random
import string

WORDLIST_FILENAME = 'palavras.txt'
ATTEMPTS = 8

# class HangMan(object):
#     '''
#     docstring for [object Object].
#     '''
#
#     guesses = 0
#     secretWord = ''
#     lettersGuessed = []
#
#     def __init__(self):
#         self.guesses = 8

def differentLetters(secretWord):
    count = 0
    differentLetters = []
    for letter in secretWord:
        if not letter in differentLetters:
            count += 1
            differentLetters.append(letter)
        else:
            pass

    return count

def choiceWord(wordlist):
    while True:
        secretWord = random.choice(wordlist).lower()
        if differentLetters(secretWord) <= ATTEMPTS:
            break

    return secretWord

def loadWords():
    '''
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print '  ', len(wordlist), 'words loaded.'

    return choiceWord(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getAvailableLetters(available, lettersGuessed):
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    print 'Available letters', available

    return available

def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'

    return guessed

def verifyLetterGuessed(guesses, secretWord, lettersGuessed):
    letter = raw_input('Please guess a letter: ')

    if letter in lettersGuessed:
        guessed = getGuessedWord(secretWord, lettersGuessed)
        print 'Oops! You have already guessed that letter:', guessed
    elif letter in secretWord:
        lettersGuessed.append(letter)
        guessed = getGuessedWord(secretWord, lettersGuessed)
        print 'Good Guess:', guessed
    else:
        guesses -= 1
        lettersGuessed.append(letter)
        guessed = getGuessedWord(secretWord, lettersGuessed)
        print 'Oops! That letter is not in my word:',  guessed
    print '------------'

    return guesses, lettersGuessed

def hangman(secretWord):
    guesses = ATTEMPTS
    lettersGuessed = []
    print '\nWelcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print 'But the word have', differentLetters(secretWord), 'different letters.'
    print '-------------'

    # Get a array with 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        available = getAvailableLetters(available, lettersGuessed)
        guesses, lettersGuessed = verifyLetterGuessed(guesses,
                                                      secretWord,
                                                      lettersGuessed)
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was', secretWord, '.'

if __name__ == '__main__':
    secretWord = loadWords().lower()
    hangman(secretWord)
