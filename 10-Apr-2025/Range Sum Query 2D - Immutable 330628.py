# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.p = [[0] * (cols + 1) for _ in range(rows + 1)] #prefix sum array
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.p[r][c] = self.p[r-1][c] + self.p[r][c-1] - self.p[r-1][c-1] + matrix[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        range_sum = self.p[row2 + 1][col2 + 1] - self.p[row2 + 1][col1] - self.p[row1][col2 + 1] + self.p[row1][col1]

        return range_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)