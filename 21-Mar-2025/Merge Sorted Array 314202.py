# Problem: Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-plaholdere instead.
        """
        seeker1 = m - 1
        seeker2 = n - 1
        holder = len(nums1)-1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        
        while seeker2 >= 0:
            if seeker1 >= 0 and nums1[seeker1] > nums2[seeker2]:
                nums1[holder] = nums1[seeker1]
                seeker1 -= 1
            else:
                nums1[holder] = nums2[seeker2]
                seeker2 -= 1
            holder -= 1