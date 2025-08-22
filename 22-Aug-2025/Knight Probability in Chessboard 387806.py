# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # 8 knight moves
        moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        P = 1.0 / 8.0

        # dp_prev[r][c] = prob to stay after `step-1` moves from (r,c)
        dp_prev = [[1.0 for _ in range(n)] for _ in range(n)]  # step = 0

        for _ in range(k):
            dp_curr = [[0.0 for _ in range(n)] for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    s = 0.0
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            s += dp_prev[nr][nc]  # only valid landings contribute
                    dp_curr[r][c] = s * P
            dp_prev = dp_curr  # roll

        return dp_prev[row][column]