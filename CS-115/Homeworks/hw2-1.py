'''
Created on: September 1, 2017
@author:   Himanshu Rana - hrana2
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

@author: Nicholas Percivale - nperciva
Pledge: "I pledge my honor that I have abided by the Stevens Honor System" 

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
from pip._vendor.html5lib._ihatexml import letter
from ctypes.wintypes import WORD

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    """This function takes a letter and returns the value of the letter by checking the scorelist"""
    if scorelist == []: 
        return 0
    first_index = scorelist[0]
    if first_index[0] == letter: 
        return first_index[1]
    return letterScore(letter, scorelist[1:])
print(letterScore("a", scrabbleScores))


def wordScore(S, scorelist):
    """This function takes in a string and returns the value of all the letters combined within the string"""
    if S == "": 
        return 0 
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
print(wordScore("spam", scrabbleScores))


def scoreList(Rack):
    """This function takes in a list of letters and returns all the words that can be made by those letters and the value of the word"""
    words = test_word(Rack, Dictionary)
    return check_dictionary(words)


def bestWord(Rack):
    """This function takes in a list of letters and returns the best word(word with the highest value)"""
    if Rack == '': 
        return 0 
    return most_points(scoreList(Rack))



def most_points(L):
    """This function finds the word with the most points within a list"""
    if len(L) == 0: 
         return ['', 0]
    elif (len(L)==1):
         return L[0]
    elif (L[0][1] > L[1][1]):
        L[1] = L[0]
        return most_points(L[1:])
    else:
        L[0] = L[1]
        return most_points(L[1:])


def test_word(Rack, L):
    """This function checks words with the rack and sees if it is possible to create the word"""
    if L == []:
         return L
    elif '0' not in check_rack(Rack,L[0]):
        return [L[0]] + test_word(Rack,L[1:])
    return test_word(Rack,L[1:])
    

def check_dictionary(S):
    """This function checks to see if the string S is in the dictionary"""
    if S == []:
        return []
    elif S[0] == '':
        return []
    elif S[0] in Dictionary:
        return [[S[0]] + [wordScore(S[0],scrabbleScores)]] + check_dictionary(S[1:])
    return check_dictionary(S[1:])


def remove(e, L):
    """This function removes the first occurrence of the e in the list provided"""
    if L == []:
         return []
    elif (L[0] != e):
        return [L[0]] + remove(e,L[1:])
    return L[1:]
    

def check_rack(Rack, S):
    """This function checks to see if the string can be created by the letters within the Rack"""
    if S == '':
        return ''
    elif S[0] in Rack:
        NewRack = remove(S[0],Rack)
        n = check_rack(NewRack,S[1:])
        return S[0] + n
    return '0'
        
print(scoreList(['a', 's', 'm', 't', 'p'])) 
print(scoreList(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z'])) 
print(bestWord(['a', 's', 'm', 't', 'p'])) 