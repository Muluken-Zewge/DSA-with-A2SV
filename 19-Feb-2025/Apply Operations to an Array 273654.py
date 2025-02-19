# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                #assign pointers to track the next non-zero element to swap
                left_pointer, right_pointer = i, len(nums) - 1
                while left_pointer < right_pointer:
                    if nums[right_pointer] != 0:
                        nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                    right_pointer -= 1

        return nums