import random
import string

WORDLIST_FILENAME = 'words.txt'
ATTEMPTS = 8

class Hangman(object):

    guesses = 0
    secretWord = ''
    lettersGuessed = []

    def __init__(self):
        self.guesses = ATTEMPTS
        self.secretWord = self.loadWords()
        self.startHangman()

    def choiceWord(self, wordlist):
        while True:
            secretWord = random.choice(wordlist).lower()
            if self.differentLetters() <= ATTEMPTS:
                break

        return secretWord

    def loadWords(self):
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

        return self.choiceWord(wordlist)

    def intro(self):
        print '\nWelcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secretWord), 'letters long.'
        print 'But the word have', self.differentLetters(), 'different letters.'
        print '-------------'

    def differentLetters(self):
        count = 0
        differentLetters = []
        for letter in self.secretWord:
            if not letter in differentLetters:
                count += 1
                differentLetters.append(letter)
            else:
                pass

        return count

    def isWordGuessed(self):
        for letter in self.secretWord:
            if not letter in self.lettersGuessed:
                return False
            else:
                pass

        return True

    def getAvailableLetters(self, available):
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        print 'Available letters', available

        return available

    def getGuessedWord(self):
        guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_'

        return guessed

    def verifyLetterGuessed(self):
        letter = raw_input('Please guess a letter: ')

        if letter in self.lettersGuessed:
            guessed = self.getGuessedWord()
            print 'Oops! You have already guessed that letter:', guessed
        elif letter in self.secretWord:
            self.lettersGuessed.append(letter)
            guessed = self.getGuessedWord()
            print 'Good Guess:', guessed
        else:
            self.guesses -= 1
            self.lettersGuessed.append(letter)
            guessed = self.getGuessedWord()
            print 'Oops! That letter is not in my word:',  guessed
        print '------------'

    def startHangman(self):
        self.intro()

        # Get a array with 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        while  self.isWordGuessed() == False and self.guesses > 0:
            print 'You have', self.guesses, 'guesses left.'
            available = self.getAvailableLetters(available)
            self.verifyLetterGuessed()
        if self.isWordGuessed() == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', self.secretWord, '.'

if __name__ == '__main__':
    hangman = Hangman()
