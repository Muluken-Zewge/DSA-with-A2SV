# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factor_sum(n):
            factor_sum = 0
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factor_sum += d
                    n //= d
                d += 1
            if n > 1: # x is prime
                factor_sum += n
            
            return factor_sum
        
        while True:
            s = prime_factor_sum(n)
            if s == n: # stable(must be prime)
                return n
            n = s
