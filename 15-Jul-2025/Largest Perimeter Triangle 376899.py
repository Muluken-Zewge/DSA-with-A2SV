# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        perimeter = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                perimeter = sum(nums[i:i+3])
        
        return perimeter
