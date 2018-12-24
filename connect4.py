'''
Created on Dec 4, 2017
Description: Connect Four Simulator
@author: Adam Undus
'''

class Board(object):
    
    def __init__(self, width=7, height=6):
        """initailize private vars"""
        self.__width = width
        self.__height = height
        self.__arrBoard = self.createArrBoard()
        self.__board = self.createBoard(self.__arrBoard)
        
    
    def createArrBoard(self):
        """create an array representation of board"""
        AB = []
        sb = []
        for _ in range(self.__height):
            for _ in range(self.__width):
                sb.append(' ')
            AB.append(sb)
            sb = []
        return AB
    
    def createBoard(self,arrBoard):
        """create string representation of board"""
        board = ''
        row = ''
        for i in range(len(arrBoard)):
            for j in range(len(arrBoard[0])):
                row += '|' + arrBoard[i][j]
            row += '|\n'
            board += row
            row = ''
        for _ in range(self.__width*2 + 1):
            board += '-'
        board += '\n'
        for z in range(self.__width):
            board += ' ' + str(z) 
        return board

        
    def __str__(self):
        """public string of board"""
        return self.__board
    
    def setBoard( self, moveString ):
        """takes in a string of columns and places alternating checkers in those columns, starting with 'X' 
        For example, call b.setBoard('012345') to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to see them alternate in the left column. moveString must be a string of integers"""
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
                if nextCh == 'X':
                    nextCh = 'O'
                else: 
                    nextCh = 'X'
    
    def allowsMove(self,col):
        """check if a move is allowed on the board"""
        if col > self.__width:
            return False
        rows = self.__arrBoard
        for r in rows:
            if r[col] == ' ':
                return True
        return False
    
    def addMove(self,col, OX): 
        """add move to the board"""   
        i = self.__height -1
        while i+1 > 0:
            if self.__arrBoard[i][col] == ' ':
                self.__arrBoard[i][col] = OX
                break
            i -= 1
        self.__board = self.createBoard(self.__arrBoard)
    
    def delMove(self,col):
        """delete a move from board"""
        i = 0
        while i < len(self.__arrBoard):
            if self.__arrBoard[i][col] != ' ':
                self.__arrBoard[i][col] = ' ' 
                break
            i += 1
        self.__board = self.createBoard(self.__arrBoard)
    
    def winsFor(self,OX):
        """check if X or O won"""
        def checkWin(r,c):
            try:
                if self.__arrBoard[r][c+1] == OX and self.__arrBoard[r][c+2] == OX and self.__arrBoard[r][c+3] == OX:
                    return True
            except:pass
            try:
                if self.__arrBoard[r+1][c] == OX and self.__arrBoard[r+2][c] == OX and self.__arrBoard[r+3][c] == OX:
                    return True
            except:pass
            try:
                if self.__arrBoard[r+1][c+1] == OX and self.__arrBoard[r+2][c+2] == OX and self.__arrBoard[r+3][c+3] == OX:
                    return True
            except:pass
            try:
                if self.__arrBoard[r+1][c-1] == OX and self.__arrBoard[r+2][c-2] == OX and self.__arrBoard[r+3][c-3] == OX:
                    return True
            except:pass
            return False 
        for i in range(len(self.__arrBoard)):
            for j in range(len(self.__arrBoard[0])):
                if self.__arrBoard[i][j] == OX:
                    if checkWin(i,j):
                        return True
        return False
    
    def hostGame(self):
        """host a game until there is a winner"""
        print('Welcome to Connect Four!')
        turn = 'X'
        while True:
            print(self)
            try:
                choice = int(input("%s's choice"%turn))
            except: 
                print('Not valid input')
                continue
            if self.allowsMove(choice):
                self.addMove(choice, turn)
            else:
                print('Move not allowed.')
            if self.winsFor(turn):
                print('%s wins -- Congratulations!'%turn)
                print(b)
                break
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            
if __name__ == "__main__":
    b = Board()
    b.hostGame()
    
    
    
