from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make a map counter for row, col, and square
            #row -> each index of board is row
            #col -> each transposed index of board is a column
            #square -> flatten board and build the squares 

        #assume true
        i = 0

        #check for the rows
        for row in board:
            check = [num for num in row if num!="."]
            counts = Counter(check)
            if counts:
                _, freq = counts.most_common(1)[0]
                if freq  > 1:
                    return False
        
        #transpose board for columns
        cols = [list(row) for row in zip(*board)]
        for col in cols:
            check = [num for num in col if num!="."]
            counts = Counter(check)
            if counts:
                _, freq = counts.most_common(1)[0]
                if freq  > 1:
                    return False

        #have create a dict with 
            #keys: box index
            #value: set of values in the box
        squares = [set() for _ in range (9)]
        for i in range(len(board)): 
            for j in range(len(board)):
                val = board[i][j]

                if val == ".":
                    continue

                square_idx = (i//3) * 3 + j//3
            
                if val in squares[square_idx]:
                    return False

                squares[square_idx].add(val)
        

            
            



        return True
