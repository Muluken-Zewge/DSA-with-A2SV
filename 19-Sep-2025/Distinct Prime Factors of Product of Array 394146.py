# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1
        for num in nums: 
            product *= num
            
        factors = set()
        d = 2
        while d * d <= product:
            while product % d == 0:
                factors.add(d)
                product //= d
            d +=1
       
        if product > 1:
            factors.add(d)

        return len(factors)