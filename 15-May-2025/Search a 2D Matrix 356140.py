# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
#consider the 2-d array like long 1-d array rows connected horizontally
#find row and colum values by quotient and module of the mid by the col number respectively
        low, high = 0, (m*n)-1
        while low <= high:
            mid = (low + high)//2
            row = mid // (n)
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False