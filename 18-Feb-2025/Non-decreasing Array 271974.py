# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num_of_violation = 0  # Count of modifications

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # Found a violation
                #if it is 1, it means the second violation
                if num_of_violation == 1:
                    return False 
                # if it is the first violation
                if i == 0 or nums[i - 1] <= nums[i + 1]:  
                    nums[i] = nums[i + 1] #(decrease it)
                else:
                    nums[i + 1] = nums[i] #(increase it)
                
                num_of_violation += 1
        
        return True  