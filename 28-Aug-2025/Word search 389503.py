# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # Base case: finished the word
            if i == len(word):
                return True
            # Out of bounds or mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            # Mark as visited (temporarily)
            temp = board[r][c]
            board[r][c] = "#"

            # Explore neighbors
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            # Restore the cell
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
