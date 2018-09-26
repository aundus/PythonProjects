'''
Created on Nov 9, 2017
Description: Game of life, where cells live and die based on those around them. 
@author: Adam Undus
'''

import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A.append(createOneRow(width)) 
    return A


def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
    return ''

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

#print(printBoard(diagonalize(7,6)))
def innerCells(width,height):
    """ Create a board with all inner cells live and all edges not"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0 or row == height-1 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(width,height):
    """ create a board with outer edges all 0s and inside is random"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0 or row == height-1 or col == width-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A
#print(printBoard(randomCells(7,6)))
def copy(board):
    A = []
    for r in board:
        A.append(r[:])
    return A
# oldA = createBoard(2, 2)
# newA = copy(oldA)
# newA[0][0] =1
# printBoard(oldA)
# printBoard(newA)

def innerReverse(board):
    """reverse all elements that are not on the outer edges of the board"""
    height = len(board)
    width = len(board[0])
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0 or row == height-1 or col == width-1:
                board[row][col] = 0
            elif board[row][col] == 0:
                board[row][col] = 1
            else:
                board[row][col] = 0
    return board
# A = randomCells(7,6)
# printBoard(A)
# innerReverse(A)
# printBoard(A)

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    def countNeighbors(r,c,A):
        count = 0
        sr = r -1 
        sc = c - 1
        for i in range(3):
            for j in range(3):        
                if A[sr+i][sc+j] == 1 and (i,j) != (1,1):
                    count += 1
        return count
    height = len(A)
    width = len(A[0])
    nA = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row != 0 and col != 0 and row != height-1 and col != width-1:
                neighbors = countNeighbors(row, col, A)
                if neighbors < 2:
                    nA[row][col] = 0
                elif neighbors > 3:
                    nA[row][col] = 0
                elif neighbors == 3 and A[row][col] == 0:
                    nA[row][col] = 1
                else:
                    nA[row][col] = A[row][col]
    return nA

# A = [ [0,0,0,0,0],
# [0,0,1,0,0],
# [0,0,1,0,0],
# [0,0,1,0,0],
# [0,0,0,0,0]]
# A2 = nextLifeGeneration(A)
# print('___')
# printBoard(A2)
# A3 = nextLifeGeneration(A2)
# print('___')
# printBoard(A3)        