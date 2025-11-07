# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        smallest = float('inf')
        total_sum = 0
        neg_nums = 0
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                if num < 0:
                    neg_nums += 1
                total_sum += abs(num)
                smallest = min(smallest, abs(num))
        
        if neg_nums % 2 == 0:
            return total_sum
        else:
            return total_sum - 2*abs(smallest)