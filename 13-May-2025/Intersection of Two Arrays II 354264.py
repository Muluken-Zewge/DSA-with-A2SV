# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        nums1_counter = Counter(nums1)
        for num in nums2:
            if num in nums1_counter:
                ans.append(num)
                nums1_counter[num] -= 1
                if nums1_counter[num] == 0:
                    del nums1_counter[num]
        
        return ans
        