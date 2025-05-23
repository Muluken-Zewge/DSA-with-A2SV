# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Step 1: Build a map of next greater elements for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Step 2: The remaining elements in stack have no next greater
        while stack:
            next_greater[stack.pop()] = -1

        # Step 3: Build result for nums1 using the map
        return [next_greater[num] for num in nums1]
        