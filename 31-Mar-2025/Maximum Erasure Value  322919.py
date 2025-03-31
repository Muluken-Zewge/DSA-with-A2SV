# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        unique_nums = set()
        left, right = 0, 0
        window_score = 0
        for right in range(len(nums)):
            if nums[right] not in unique_nums:
                window_score += nums[right]
                unique_nums.add(nums[right])
            else:
                while nums[right] in unique_nums:
                    window_score -= nums[left]
                    unique_nums.remove(nums[left])
                    left += 1
                window_score += nums[right]
                unique_nums.add(nums[right])

            max_score = max(max_score, window_score)

        return max_score