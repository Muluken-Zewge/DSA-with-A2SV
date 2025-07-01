# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0
        
        def inbound(row,col):
            return (0 <= row < rows) and (0 <= col < cols)

        def dfs(row, col):
            if not inbound(row,col) or grid[row][col] == '0':
                return
            grid[row][col] = '0' # mask as visited 

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                dfs(new_row, new_col)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    #this dfs call will cover all land connected to the cell grid[i][j]
                    dfs(i,j)
        
        return islands