# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num   # xor of two unique numbers

        # find rightmost set bit
        diff = xor & -xor  

        a, b = 0, 0
        for num in nums:
            if num & diff:
                a ^= num  # group A
            else:
                b ^= num  # group B
        
        return [a, b]
