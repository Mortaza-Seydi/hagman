# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
import string
from random import randrange
from string import *
import hangman_lib

WORDLIST_FILENAME = "words.txt"


# def load_words():
#     """
#     Returns a list of valid words. Words are strings of lowercase letters.
#
#     Depending on the size of the word list, this function may
#     take a while to finish.
#     """
#     print("Loading word list from file...")
#     # inFile: file
#     inFile = open(WORDLIST_FILENAME, 'r')
#     # line: string
#     line = inFile.readline()
#     # wordlist: list of strings
#     wordlist = line.split()
#     print("  ", len(wordlist), "words loaded.")
#     print('Enter play_hangman() to play a game of hangman!')
#     return wordlist
#
#
# # actually load the dictionary of words and point to it with
# # the words_dict variable so that it can be accessed from anywhere
# # in the program
# words_dict = load_words()
#
#
# # Run get_word() within your program to generate a random secret word
# # by using a line like this within your program:
# # secret_word = get_word()
#
# def get_word():
#     """
#     Returns a random word from the word list
#     """
#     word = words_dict[randrange(0, len(words_dict))]
#     return word


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap'
letters_guessed = []
mistakes_made = 0
letter_domain = list(string.ascii_lowercase)
guessed_word = ''


def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed
    counter = 0
    result = False
    for a in letters_guessed:
        if a in secret_word:
            counter += 1
    if counter == get_number_of_letters(secret_word):
        result = True
    return result


def print_guessed(guessed_letter):
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    global guessed_word
    i = 0
    for a in secret_word:
        if a == guessed_letter:
            guessed_word = guessed_word[:i] + guessed_letter + guessed_word[i + 1:]
        i += 1
    print(guessed_word)


def random_letter():
    '''
    generate random letter to guess word
    '''

    letter = letter_domain[randrange(0, len(letter_domain))]
    return letter


def letter_checker(guessed_letter):

    global letters_guessed
    global mistakes_made
    global letter_domain
    print('guessed_letter : ',guessed_letter)
    letters_guessed.append(guessed_letter)
    if guessed_letter in secret_word:
        letter_domain.remove(guessed_letter)
    else:
        mistakes_made += 1
    print_guessed(guessed_letter)


def get_number_of_letters(word):
    return len(set(word))


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    global guessed_word
    # Put the mistakes_made variable here, since you'll only use it in this function

    result = False

    # Update secret_word.
    # secret_word  = get_word()

    for _ in secret_word:
        guessed_word += '-'

    while mistakes_made < MAX_GUESSES:
        guessed_letter = random_letter()
        letter_checker(guessed_letter)
        if len(letters_guessed) >= get_number_of_letters(secret_word):
            result = word_guessed()

        if result:
            break

    hangman_lib.print_hangman_image(mistakes_made)

    return None


play_hangman()
