# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for holder in range(len(nums)):
            seeker = holder + 1
            while seeker < len(nums):
                if nums[holder] == 0 and nums[seeker] != 0:
                    nums[holder], nums[seeker] = nums[seeker], nums[holder]
                    break
                elif nums[holder] != 0:
                    break
                seeker += 1