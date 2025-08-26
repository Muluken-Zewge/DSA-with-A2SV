# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        prev = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > prev:
                parts = math.ceil(nums[i] / prev)
                operations += parts - 1
                prev = nums[i] // parts
            else:
                prev = nums[i]

        return operations
