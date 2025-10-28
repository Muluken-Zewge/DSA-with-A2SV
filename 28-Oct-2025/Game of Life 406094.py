# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        status = [[0 for i in range(col)] for j in range(row)]
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        def is_inbound(r,c):
            return (0 <= r < row) and (0 <= c < col)
        
        for i in range(row):
            for j in range(col):
                alives = 0
                for r,c in directions:
                    nr = r + i
                    nc = c + j
                    if is_inbound(nr,nc) and board[nr][nc] == 1:
                        alives += 1
                if board[i][j] == 0:
                    if alives == 3:
                        status[i][j] = 1
                elif board[i][j] == 1:
                    if alives < 2 or alives > 3:
                        status[i][j] = -1
        for i in range(row):
            for j in range(col):
                board[i][j] += status[i][j]