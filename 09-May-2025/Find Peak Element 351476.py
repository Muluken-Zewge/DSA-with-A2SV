# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right  = 0, n-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left
        