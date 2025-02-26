# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        treshold = len(nums)/3

        nums = [num for num in nums_counter if nums_counter[num] > treshold]

        return nums