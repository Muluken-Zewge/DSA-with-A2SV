# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for left in range(len(nums)):
            right = left + 1
            while right < len(nums):
                if nums[left] + nums[right] < target:
                    count += 1
                    right += 1
                else:
                    break

        return count