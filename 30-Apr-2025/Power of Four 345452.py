# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #base cases
        if n == 1:
            return True
        if n < 1:
            return False
        
        return self.isPowerOfFour(n/4) #recursive relation