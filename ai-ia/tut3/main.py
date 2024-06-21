from NQueen.NQueens import NQueens

def nqueen_solve():
    # using min-conflict algorithm
    n = 8
    NQ = NQueens(n)
    timer = 0
    while not NQ.allQueensSafe():
        minAttacks = n + 1
        pickedQueen = NQ.pickRandomQueen()
        
        pos = NQ.availablePosition(pickedQueen)
        minConflictPosition = pickedQueen 
        for p in pos:
            NQ.moveQueen(pickedQueen, p)
            newNumberOfConflicts = NQ.specificQueenConflicts(p)
            if newNumberOfConflicts < minAttacks:
                minConflictPosition = p
                minAttacks = newNumberOfConflicts
            NQ.moveQueen(p, pickedQueen) 
        
        NQ.moveQueen(pickedQueen, minConflictPosition)
        timer += 1  
    
    NQ.printBoard()
    print(f"Solved in {timer} iterations")
            

if __name__ == "__main__":
    nqueen_solve()
