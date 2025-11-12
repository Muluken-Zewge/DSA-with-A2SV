# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # store the number and it's index in a dictionary
        num_index = {}
        for i, num in enumerate(nums):
            num_index[num] = i

        for num1,num2 in operations:
            index = num_index[num1]
            nums[index] = num2
            num_index[num2] = index # update index value
        
        return nums