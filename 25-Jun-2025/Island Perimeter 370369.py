# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def inbound(row, col):
            return (0 <= row < rows) and (0 <= col < cols)
        
        def dfs(grid, visited, row, col):
            visited[row][col] = True
            perimeter = 0

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                elif not visited[new_row][new_col]:
                    perimeter += dfs(grid, visited, new_row, new_col)
                
            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(grid, visited, r, c)