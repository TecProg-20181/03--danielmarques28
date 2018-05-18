from __future__ import print_function
import random
import string
import sys

WORDLIST_FILENAME = 'words.txt'
ATTEMPTS = 8

class Hangman(object):

    guesses = 0
    secret_word = ''
    letters_guessed = []

    def __init__(self):
        '''
        Construct method of Hangman class
        '''
        self.guesses = ATTEMPTS
        self.secret_word = self.load_words()
        self.start_hangman()

    def choice_word(self, wordlist):
        '''
        Choice a ramdom word of wordlist
        '''
        while True:
            secret_word = random.choice(wordlist).lower()
            if self.different_letters() <= ATTEMPTS:
                break
            print('Choosing another word')

        return secret_word

    def load_words(self):
        '''
        Depending on the size of the word list, this function may
        take a while to finish.
        '''
        print('Loading word list from file...')
        # inFile: file
        in_file = open(WORDLIST_FILENAME, 'r')
        # line: string
        line = in_file.readline()
        # wordlist: list of strings
        wordlist = line.split()
        if len(wordlist) == 0:
            print('The file of words is empty')
            sys.exit(0)
        else:
            print('  ', len(wordlist), 'words loaded.')
            return self.choice_word(wordlist)

    def intro(self):
        '''
        Print the intro of the Hangman game
        '''
        print('\nWelcome to the game, Hangam!')
        print('I am thinking of a word that is', len(self.secret_word), 'letters long.')
        print('But the word have', self.different_letters(), 'different letters.')
        print('-------------')

    def different_letters(self):
        '''
        Count the differents letter in the secret word
        '''
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
        '''
        Verify if the letter guessed was guessed before
        '''
        for letter in self.secret_word:
            if not letter in self.letters_guessed:
                return False
            else:
                pass

        return True

    def get_available_letters(self, available):
        '''
        Get the letters that still available to guess
        '''
        for letter in available:
            if letter in self.letters_guessed:
                available = available.replace(letter, '')
        
        return available

    def get_guessed_word(self):
        '''
        Get the letters guessed that was in the secret word
        '''
        guessed = ''
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                guessed += letter
            else:
                guessed += '_'

        return guessed

    def is_letter(self, letter):
        '''
        Validate if the content of string is a letter
        '''
        try:
            int(letter)
            print('\nThe letter can\'t be a number !\n')
            return False
        except ValueError:
            return True

    def len_of_one(self, letter):
        '''
        Validate if the len of letter is one
        '''
        if len(letter) == 1:
            return True
        elif len(letter) == 0:
            print('\nNo letter guessed\n')
            return False
        else:
            print('\nCan\'t guess more than one letter\n')
            return False
        
    def validate_letter(self, letter):
        '''
        Call the sub validations methods (is_letter and len_of_one)
        '''
        if self.is_letter(letter):
            return self.len_of_one(letter)
        else:
            return False
        
    def read_letter_guessed(self):
        '''
        Read the input (letter guessed) in python 2.x and 3.x
        '''
        while True:
            print('Please guess a letter: ', end='')
            try: 
                letter = raw_input().lower()
            except NameError:
                letter = input().lower()
                pass
            
            if self.validate_letter(letter):
                break

        self.verify_letter_guessed(letter)

    def verify_letter_guessed(self, letter):
        '''
        Verify if the input was already guessed, the correct letter
        or the incorrent letter
        '''
        try:
            assert isinstance(letter, str) and len(letter) == 1
        except AssertionError:
            print('The letter has to be string and len of 1')
            sys.exit(0)
        
        if letter in self.letters_guessed:
            guessed = self.get_guessed_word()
            print('Oops! You have already guessed that letter:', guessed)
        elif letter in self.secret_word:
            self.letters_guessed.append(letter)
            guessed = self.get_guessed_word()
            print('\nGood Guess:', guessed)
        else:
            self.guesses -= 1
            self.letters_guessed.append(letter)
            guessed = self.get_guessed_word()
            print('Oops! That letter is not in my word:',  guessed)
        print('------------')

    def start_hangman(self):
        '''
        Start the Hangman game
        '''
        self.intro()

        # Get a array with 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        while  self.is_word_guessed() == False and self.guesses > 0:
            print('You have', self.guesses, 'guesses left.')
            available = self.get_available_letters(available)
            print('Available letters', available)
            self.read_letter_guessed()
        if self.is_word_guessed() == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was', self.secret_word + '.')

if __name__ == '__main__':
    hangman = Hangman()
