# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k is larger than n
        
        nums.reverse() # Reverse the entire array
        nums[:k] = reversed(nums[:k])  # Reverse the first k elements
        nums[k:] = reversed(nums[k:]) # Reverse the remaining elements