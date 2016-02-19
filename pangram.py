#! /usr/bin/python3
''' 
panogram.py - this program recongizes pangrams.
by zorba
'''

import sys


def pangram_check(sentence_or_word):
    '''
    checks the user input to see if it is a pangram.
    '''

    letters = set('abcdefghijklmnopqrstuvwxyz')

    if sentence_or_word.lower() == 'done':
        z

    for letter in sentence_or_word.lower():
        if letter in letters:
            letters.remove(letter)
    
    if len(letters) == 0:
        print('\nThe sentence or word is a panogram!')
    
    else:
        print('\nThis sentence or word is not a panogram.')


def main():
    '''
    main
    '''
    sentence_or_word = input('\nPlease enter a sentence or a word to check to see if it is a pangram: \nIf Done, Please type Done')

    pangram_check(sentence_or_word)


if __name__ == '__main__':
    sys.exit(main())

