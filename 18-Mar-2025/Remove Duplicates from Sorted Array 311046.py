# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0 # to track index of unique elements

        # to look for a unique element
        for seeker in range(1,len(nums)):
            if nums[holder] != nums[seeker]:
                holder += 1
                nums[holder] = nums[seeker]
        
        return holder + 1 