# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        colums = len(matrix[0])
        transposed = [[0]*rows for _ in range(colums)]
        for r in range(rows):
            for c in range(colums):
                transposed[c][r] = matrix[r][c]
        
        return transposed