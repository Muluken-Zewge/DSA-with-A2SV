# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = sub_array_sum = 0

        for right in range(len(nums)):
            sub_array_sum += nums[right]
            while sub_array_sum >= target:
                min_length = min(min_length, right - left + 1)
                sub_array_sum -= nums[left]
                left += 1
            
        return min_length if min_length != float('inf') else 0