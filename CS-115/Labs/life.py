#
# life.py - Game of Life lab
#
# Name: Himanshu Rana 
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
#

import random
import sys


def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Returns a 2d array with "height" rows and "width" cols"""
    A = []
    for row in range(height): 
        A += [createOneRow(width)]
    return A 

#A = createBoard(5, 3) 
#print(A) 

def printBoard( A ):
    """ this function prints the 2d list-of-lists A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
    
#A = createBoard(5, 3) 
#printBoard(A)


def diagonalize(width,height):
    """ creates an empty board and then modifies it so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

#A = diagonalize(7, 6)
#printBoard(A)

def innerCells(w, h):
    A = createBoard(w, h)
    for row in range(h): 
        for col in range(w): 
            if 0 < row < h - 1 and 0 < col < w - 1: 
                A[row][col] = 1
            else: 
                A[row][col] = 0
    return A 

#A = innerCells(5, 5)
#printBoard(A)

def randomCells(w, h):
    A = createBoard(w, h)
    for row in range(h): 
        for col in range(w): 
            A[row][col] = random.choice([0, 1])
    return A 

#A = randomCells(10, 10)
#printBoard(A)  

def copy(A):
    height = len(A)
    width = len(A[0])
    B  = createBoard(width, height) 
    for row in range(height): 
        for col in range(width): 
            B[row][col] = A[row][col]
    return B  

#oldA = createBoard(2, 2)
#printBoard(oldA)

#newA = oldA 
#printBoard(newA)

#oldA[0][0] = 1 
#printBoard(oldA)

#printBoard(newA)

def innerReverse(A):
    for row in range(len(A)): 
        for col in range(len(A[0])): 
            if 0 < row < len(A) - 1 and 0 < col < len(A[0]): 
                A[row][col] = (A[row][col] + 1) % 2 
            else: 
                A[row][col] = 0 
    return A 
#A = randomCells(8, 8)
#printBoard(A)

#A2 = innerReverse(A)
#printBoard(A2)

def countNeighbors(row, col, A):
    count = 0 
    if A[row - 1][col - 1] == 1:
        count += 1 
    if A[row - 1][col] == 1: 
        count += 1
    if A[row - 1][col + 1] == 1: 
        count += 1
    if A[row][col - 1] == 1: 
        count += 1 
    if A[row][col + 1] == 1: 
        count += 1
    if A[row + 1][col - 1] == 1: 
        count += 1
    if A[row + 1][col] == 1: 
        count += 1
    if A[row + 1][col + 1] == 1: 
        count += 1
    return count
        

def next_life_generation(A):
    """ makes a copy of A and then advanced one generation of 
    Conway's game of life within the *inner cells* of that copy. 
    The outer edge always stays 0."""
    newA = copy(A)
    for row in range(1, len(A) - 1): 
        for col in range(1, len(A[row]) - 1):
            if countNeighbors(row, col, A) < 2 or countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and countNeighbors(row, col, A) == 3: 
                newA[row][col] = 1
            else: 
                newA[row][col] = A[row][col]
    return newA 
            
    
A = [[0,0,0,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0]]

printBoard(A)





