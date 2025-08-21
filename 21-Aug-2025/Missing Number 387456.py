# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for num in range(len(nums)+1):
        #     if num not in set(nums):
        #         return num

        #bit manipulation approach
        n = len(nums)
        res = 0
        # XOR all indices + nums
        for i in range(n + 1):
            res ^= i
        for num in nums:
            res ^= num
        return res