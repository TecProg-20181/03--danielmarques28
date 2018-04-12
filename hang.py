import random
import string

WORDLIST_FILENAME = 'words.txt'
ATTEMPTS = 8

class Hangman(object):

    guesses = 0
    secret_word = ''
    letters_guessed = []

    def __init__(self):
        self.guesses = ATTEMPTS
        self.secret_word = self.load_words()
        self.start_hangman()

    def choice_word(self, wordlist):
        while True:
            secret_word = random.choice(wordlist).lower()
            if self.different_letters() <= ATTEMPTS:
                break
            print 'Choosing another word'

        return secret_word

    def load_words(self):
        '''
        Depending on the size of the word list, this function may
        take a while to finish.
        '''
        print 'Loading word list from file...'
        # inFile: file
        in_file = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        line = in_file.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        print '  ', len(wordlist), 'words loaded.'

        return self.choice_word(wordlist)

    def intro(self):
        print '\nWelcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secret_word), 'letters long.'
        print 'But the word have', self.different_letters(), 'different letters.'
        print '-------------'

    def different_letters(self):
        count = 0
        different_letters = []
        for letter in self.secret_word:
            if not letter in different_letters:
                count += 1
                different_letters.append(letter)
            else:
                pass

        return count

    def is_word_guessed(self):
        for letter in self.secret_word:
            if not letter in self.letters_guessed:
                return False
            else:
                pass

        return True

    def get_available_letters(self, available):
        for letter in available:
            if letter in self.letters_guessed:
                available = available.replace(letter, '')
        print 'Available letters', available

        return available

    def get_guessed_word(self):
        guessed = ''
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                guessed += letter
            else:
                guessed += '_'

        return guessed

    def verify_letter_guessed(self):
        letter = raw_input('Please guess a letter: ')

        if letter in self.letters_guessed:
            guessed = self.get_guessed_word()
            print 'Oops! You have already guessed that letter:', guessed
        elif letter in self.secret_word:
            self.letters_guessed.append(letter)
            guessed = self.get_guessed_word()
            print 'Good Guess:', guessed
        else:
            self.guesses -= 1
            self.letters_guessed.append(letter)
            guessed = self.get_guessed_word()
            print 'Oops! That letter is not in my word:',  guessed
        print '------------'

    def start_hangman(self):
        self.intro()

        # Get a array with 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        while  self.is_word_guessed() == False and self.guesses > 0:
            print 'You have', self.guesses, 'guesses left.'
            available = self.get_available_letters(available)
            self.verify_letter_guessed()
        if self.is_word_guessed() == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', self.secret_word, '.'

if __name__ == '__main__':
    hangman = Hangman()
