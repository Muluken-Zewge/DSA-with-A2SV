# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

#use binary search of 'search on output space' varient
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #function to check if a given divisor can be a valid divisor
        def can_be_divisor(divisor):
            division_sum = 0
            for num in nums:
                division_sum += ceil(num/divisor)
            
            return division_sum <= threshold

        #binary search for minimzing valid divisors
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right)//2
            if can_be_divisor(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            