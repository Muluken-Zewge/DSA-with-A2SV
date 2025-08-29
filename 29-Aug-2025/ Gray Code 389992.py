# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(2**n):
            gray = i ^ (i >> 1)
            ans.append(gray)
        
        return ans