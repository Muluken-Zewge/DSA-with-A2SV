# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        d = 2
        factors = []
        while d * d <= n:
            if n % d == 0:
                factors.append(d)
                if (n//d) not in factors:
                    factors.append(n//d)
            d += 1
        factors.append(1)
        factors.append(n)
        factors.sort()
        if k > len(factors):
            return -1
        
        return factors[k-1]
        