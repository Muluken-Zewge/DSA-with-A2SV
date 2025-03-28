# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix = 0  # Keeps track of the smallest prefix sum seen so far
        max_sum = float('-inf')  # Stores the maximum subarray sum
        prefix_sum = 0  # Running prefix sum

        for num in nums:
            prefix_sum += num  # Update prefix sum
            # Compute max subarray sum
            max_sum = max(max_sum, prefix_sum - min_prefix)  
            min_prefix = min(min_prefix, prefix_sum)  # Update min prefix sum
        
        return max_sum