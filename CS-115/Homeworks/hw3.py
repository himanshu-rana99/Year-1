'''
Created on September 24, 2017
@author:   hrana2 - Himanshu Rana 
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System" 

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(change, lst):
    ''' This function will take in an input as change and return a list 
        with the minimum number of coins needed to make the change and the 
        a list of the coins '''
    if change == 0: 
        return [0, []]
    if lst == []: 
        return [float('inf'), []]
    if lst[0] > change:
        return giveChange(change, lst[1:])
    [use_it_num, use_it] = giveChange(change - lst[0], lst)
    [lose_it_num, lose_it] = giveChange(change, lst[1:])
    if use_it_num + 1 < lose_it_num: 
        use_it.append(lst[0])
        return [use_it_num + 1, use_it]
    return [lose_it_num, lose_it]
        
print(giveChange(48, [1, 5, 10, 25, 50]))
    
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    
    if dct == []: 
        return []
    if scores == []: 
        return ["", 0]
    return [dct[0], wordScore(dct[0], scores)] + wordsWithScore(dct[1:], scores)
    
    
def letterScore(letter, scorelist):
    """This function takes a letter and returns the value of the letter by checking the scorelist"""
    if scorelist == []: 
        return 0
    first_index = scorelist[0]
    if first_index[0] == letter: 
        return first_index[1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """This function takes in a string and returns the value of all the letters combined within the string"""
    if S == "": 
        return 0 
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

print(wordsWithScore(Dictionary, scrabbleScores))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    def take_helper(n, L, count, lst):
        if n == count: 
            return lst 
        lst = lst + [L[0]]
        return take_helper(n, L[1:], count + 1, lst)
    if L == [] or n == 0: 
        return [] 
    return take_helper(n, L, 0, [])
   
    
print(take(0, [1, 2, 3, 4, 5]))



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L == []: 
        return [] 
    if n == 0: 
        return L 
    return drop(n-1, L[1:])

   
print(drop(1, [1, 2, 3, 4, 5]))


