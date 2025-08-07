# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for row_num in range(rowIndex + 1):
            row = [1] * (row_num + 1)

            for col in range(1, row_num):
                row[col] = result[row_num - 1][col-1] + result[row_num - 1][col]
                
            result.append(row)
        
        return result[-1]