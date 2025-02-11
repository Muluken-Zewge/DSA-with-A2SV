# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #product of top 3 elements
        max_product1 = nums[-1] * nums[-2] * nums[-3]
        #product of two smallest and the largest element
        max_product2 = nums[0] * nums[1] * nums[-1]
        #compare the two products
        max_product = max(max_product1, max_product2)

        return max_product
        