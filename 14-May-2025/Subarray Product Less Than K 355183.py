# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        prod = 1
        ans = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        
        return ans