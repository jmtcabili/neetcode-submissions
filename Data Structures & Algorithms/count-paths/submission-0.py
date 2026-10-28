class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #pre fill grid with 0s
        row = m
        col = n
        grid = [[1] * col] * row

        #fill up table 
        for i in range (row-2, -1, -1): 
            for j in range (col-2, -1, -1): 
                right = grid[i][j+1]
                down = grid[i+1][j]
                grid[i][j] = right + down
        
        return grid[0][0]
        
        