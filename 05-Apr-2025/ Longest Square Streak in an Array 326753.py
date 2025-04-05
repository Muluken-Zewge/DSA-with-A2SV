# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        longest = 1
        for i in range(len(nums)):
            current_longest = 1
            num = nums[i]
            while num ** 2 in nums_set:
                current_longest += 1
                num = num ** 2
            longest = max(longest, current_longest)

        return longest if longest > 1 else -1