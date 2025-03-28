# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = {0: -1}  
        prefix_sum = 0  

        for i, num in enumerate(nums):
            prefix_sum += num 
            remainder = prefix_sum % k 

            if remainder in prefix_mod:
              
                if i - prefix_mod[remainder] > 1:
                    return True
            else:
                prefix_mod[remainder] = i 

        return False