# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_of_row = len(matrix)
        #tronspose the matrix in-place
        for i in range(num_of_row):
            for j in range(i+1, num_of_row):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        #swap elements in each row   
        for i in range(num_of_row):
            left = 0
            right = num_of_row-1
            while left < right:
                matrix[i][left], matrix[i][right] =  matrix[i][right], matrix[i][left]
                left +=1
                right-=1