# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        ans = []
        #sort the list using bubble sort
        for i in range(size):
            swapped = False #to stop if the array is already sorted
            for j in range(size -i -1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1], nums[j]
                    swapped = True

            if not swapped:
                break
        
        for i in range(size):
            if nums[i] == target:
                ans.append(i)

        return ans
