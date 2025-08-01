# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(index,current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            key = (index, current_sum)
            if key in memo:
                return memo[key] 

            add = dp(index + 1, current_sum + nums[index])
            sub = dp(index + 1, current_sum - nums[index])
            
            memo[key] = add + sub

            return memo[key]
            
        return dp(0,0)