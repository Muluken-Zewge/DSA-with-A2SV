# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums)) # to remove duplicates
        unique_nums.sort()

        if len(unique_nums) >= 3:
            return unique_nums[-3]
        else:
            return unique_nums[-1]
