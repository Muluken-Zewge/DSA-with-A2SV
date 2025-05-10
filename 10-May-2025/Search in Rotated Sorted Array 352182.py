# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

#since the rotated array was sorted, after rotation there'll be two sorted sub arrays. in each iteration, we'll find the sorted part and check if the target is in it or not. according to that, we half our search space.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            #check whic part is sorted
            if nums[mid] >= nums[left]:#left side is soretd
                #check if target is in the sorted part
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:#right side is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1