# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        if len(nums) == 0:
            return 0
        while i >= 0:
            j = i - 1
            while j >= 0:
                if nums[j] == val:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
                j -= 1
            i -= 1
        count = 0
        for num in nums:
            if num != val:
                count += 1
        
        return count