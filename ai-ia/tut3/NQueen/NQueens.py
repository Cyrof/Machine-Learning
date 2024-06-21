import random 

class NQueens:
    def __init__(self, n):
        """
        Initialise the NQueens object with a board of size n
        :param n: int - the size of the board (n x n) and the number of queens
        """
        self.board, self.queenPositions = self.getNewBoard(n)
        self.n = n
        
    def getNewBoard(self, n):
        """
        Create a new n x n board with one queen placed randomly in each row
        :param n: int - the size of the board (n x n) and the number of queens
        :return (board, queenPos): a tuple containing the board (a list of lists) and the list of queen positions
        """
        board = []
        queenPos = []
        for x in range(n):
            board.append([0]*n)
            
        for x in range(n):
            randomIndex = random.randint(0,n-1)
            board[x][randomIndex] = 1
            queenPos.append((x, randomIndex))
            
        return (board, queenPos)
    
    def allQueensSafe(self):
        """
        Check if all queens are safe 
        :param:
        :return bool: True is all queens are safe. false otherwise
        """
        for pos in self.queenPositions:
            if(self.underAttack(pos)):
                return False
        return True
    
    def underAttack(self, pos):
        """
        Check if the queen at the given position is under attack 
        :param pos: tuple - the position of the queen to check (row, column)
        :return bool: True is the queen is under attack, false otherwise 
        """
        if(self.attackViaDiagonal(pos)):
            return True
        
        if(self.attackViaRow(pos)):
            return True
        
        if(self.attackViaCol(pos)):
            return True

        return False
    
    def attackViaCol(self, pos):
        """
        Check for attacks via the column of the given position
        :param pos: the position of the queen to check (row, col)
        :return bool: true is there is another queen in the same col, false otherwise 
        """
        for queen in self.queenPositions:
            if(pos[1] == queen[1] and queen != pos):
                return True
        return False
    
    def attackViaRow(self, pos):
        """
        check for attacks via the row of the given position 
        :param pos: the position of the queen to check (row, col)
        :returns bool: true if there is another queen in the same row, false otherwise 
        """
        for queen in self.queenPositions:
            if(pos[0] == queen[0] and queen != pos):
                return True
        return False

    def attackViaDiagonal(self, pos):
        """
        check for attacks via the diagonals of the given position
        :param pos: the position of the queen to check (row, col)
        :return bool True if there is another queen on the same diagonal, false otherwise 
        """
        for queen in self.queenPositions:
            if(abs(queen[0] - pos[0]) == abs(queen[1] - pos[1]) and queen != pos):
                return True
        return False
    
    def pickRandomQueen(self):
        """
        pick a random queen from the list of queen positions
        :param: 
        :return tuple: the position of the randomly picked queen (row, col)
        """
        newIndex = random.randint(0,self.n-1)
        return self.queenPositions[newIndex]

    def availablePosition(self, pos):
        """
        get all available positions in the row of the given position
        :param pos: the position to check
        :return list: a list of available positions in the row of the given position 
        """
        availablePos = []
        for x in range(self.n):
            availablePos.append((pos[0],x))
        return availablePos
    
    def moveQueen(self, startPos, endPos):
        """
        move a queen from the start position to the end position 
        :param startPos: the starting position of the queen 
        :param endPos: the ending position of the queen 
        :raises AssertionError: if there is no queen at the start position 
        """
        assert self.board[startPos[0]][startPos[1]] == 1
        self.board[startPos[0]][startPos[1]] = 0
        self.board[endPos[0]][endPos[1]] = 1
        self.queenPositions.remove(startPos)
        self.queenPositions.append(endPos)

    def specificQueenConflicts(self, pos):
        """
        count the number of conflicts for a spcific queen 
        :param pos: the position of the queen to check 
        :return int: the number of conflicts for the queen at the given position
        :raises AssertionError: if the position does not contain a queen
        """
        assert pos in self.queenPositions
        count = 0
        for queen in self.queenPositions:
            if(abs(queen[0]-pos[0]) == abs(queen[1]-pos[1]) and queen != pos):
                count += 1
            if (pos[0] == queen[0] and queen != pos):
                count += 1
            if(pos[1] == queen[1] and queen != pos):
                count += 1
                
        return count 
    
    def printBoard(self):
        """
        Print the positions of all the queens on the board.
        """
        for queen in self.queenPositions:
            print(queen)
        print()
            