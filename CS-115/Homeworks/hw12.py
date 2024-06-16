'''
Created on Dec 6, 2017

@author: hrana2 - Himanshu Rana 
"I pledge my honor that I have abided by the Stevens Honor System" 
'''

class Board(object):
    def __init__(self, width = 7, height = 6):
        self.__width = width 
        self.__height = height
        self.__board_slot = [[' '] * width for row in range(self.__height)]
    
    def __str__(self):
        s = ''
        
        for row in range(self.__height): 
            s += '|'
            
            for col in range(self.__width): 
                s += self.__board_slot[row][col] + '|'
                
            s += '\n'
        s += (2 * self.__width + 1) * '-'
        s += '\n'
        s += ' '
        for col in range(self.__width): 
            if col > 9: 
                col = col % 10
            s += str(col)
            s += ' '
            
        return s
        
    def allowsMove(self, col):
        """This function return True if the col value has an 
        open spot for a checker to be placed in it"""
        if col < 0: 
            return False   
        elif col > self.__width - 1: 
            return False
        elif self.__board_slot[0][col] != ' ': 
            return False
        return True
        
    def addMove(self, col, ox):
        """This function adds the checker, either X or O and
         place it in the given col value"""
        if self.allowsMove(col) == True: 
            isGood = True
            col = int(col)
        for row in reversed(range(len(self.__board_slot))): 
            if self.__board_slot[row][col] != " ": 
                row += 1
            else: 
                self.__board_slot[row][col] = ox
                isGood = False
                break 
            if not isGood: 
                break 
       
            
    def setBoard(self, move_string):
        """ takes in a string of columns and places alternating 
        checkers in those columns, starting with 'X' For example, 
        call b.setBoard('012345') to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to see them alternate in 
        the left column.moveString must be a string of integers"""
        nextCh = 'X' # start by playing 'X'
        for colString in move_string:    
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': 
                nextCh = 'O'
            else: 
                nextCh = 'X'
                
    def delMove(self, col):
        """This function does the opposite of addMove in which it 
        removes the top checker from the col value"""
        isGood = True 
        for row in range(len(self.__board_slot)): 
            if self.__board_slot[row][col] == " ": 
                row += 1
            else: 
                self.__board_slot[row][col] = " "
                isGood = False
                break
            if not isGood:
                break 
        
    def winsFor(self, ox):
        """This function return True if the given checker X or O 
        has won the game. It checks for the horizontal, vertical, and diagnol cases""" 
        for row in range(self.__height):
            for col in range(self.__width - 3):
                if self.__board_slot[row][col] == self.__board_slot[row][col + 1] == self.__board_slot[row][col + 2] == self.__board_slot[row][col + 3] == ox:
                    return True
     
        for col in range(self.__width):
            for row in range(self.__height - 3):
                if self.__board_slot[row][col] == self.__board_slot[row + 1][col] == self.__board_slot[row + 2][col] == self.__board_slot[row + 3][col] == ox:
                    return True
        
        for row in range(self.__height - 3):
            for col in range(self.__width - 3):
                if self.__board_slot[row][col] == self.__board_slot[row + 1][col + 1] == self.__board_slot[row + 2][col +2 ] == self.__board_slot[row + 3][col + 3] == ox:
                    return True
        
        for row in range(self.__height - 3):
            for col in range(3, self.__width):
                if self.__board_slot[row][col] == self.__board_slot[row + 1][col - 1] == self.__board_slot[row + 2][col - 2] == self.__board_slot[row + 3][col - 3] == ox:
                    return True
        
        return False
    
    def tie_game(self):
        """This function handles the case were the game ends in a tie, where both X and O do not win"""
        return all(self.allowsMove(col) == False for col in range(self.__width))
            
            
    def hostGame(self):
        """This function will loop, allowing the player to play the game of Connect 4"""
        print("\n\nWelcome to Connect Four!\n\n")
        while True:
            print(self)
            
            userinX = int(input("\nX's choice:  "))
            print("\n")
            while self.allowsMove(userinX) == False:
                print("Not a valid move, please try again")
                userinX = int(input("\nX's choice:  "))
                print("\n")
            self.addMove(userinX,'X')
            if self.winsFor('X'):
                print("\n\nX wins -- Congratulations!\n\n")
                print(self)
                break
            else:
                print(self)
            
            userinO = int(input("\nO's choice:  "))
            print("\n")
            while self.allowsMove(userinO )== False:
                print("Not a valid move, please try again")
                userinO = int(input("\nO's choice:  "))
                print("\n")
            self.addMove(userinO,'O')
            if self.winsFor('O'):
                print("\n\nO wins -- Congratulations!\n\n")
                print(self)
                break
            if self.tie_game() == True: 
                print("Tie game -- Play another round")
                break
        

if __name__ == '__main__': 
    
    board1 = Board(7, 6)
    board1.hostGame()
   

            
        