# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0] * 2
        maximum = 0
        is_there_1 = False

        for row in range(len(mat)):
            count_of_1 = mat[row].count(1)
            if count_of_1 > maximum:
                is_there_1 = True
                maximum = count_of_1
                ans[0], ans[1] = row , maximum
        
        if not is_there_1:
            ans[0], ans[1] = 0 , 0

        return ans