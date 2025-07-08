# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m , n = len(maze), len(maze[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        queue.append((entrance[0],entrance[1],0)) #0 represtns the current step

        # helper function to check if a cell is an exit
        def isExit(row,col):
            return (row == 0 or row == m - 1) or (col == 0 or col == n - 1)

        while queue:
            r, c, step = queue.popleft()

            if (r,c) != (entrance[0],entrance[1]) and isExit(r,c):
                return step
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    queue.append((nr,nc,step+1))
                    maze[nr][nc] = '*' #mark it visited with asterisk
        
        return -1