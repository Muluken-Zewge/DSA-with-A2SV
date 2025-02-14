# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)
        set_length = len(set(nums))
        #if there is a duplicate, set doesn't consider it
        if set_length < list_len:
            return True
        else:
            return False