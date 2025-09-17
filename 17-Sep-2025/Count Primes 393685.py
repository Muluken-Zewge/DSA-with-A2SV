# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        # use Sieve of Eratosthenes algorithm
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2
        while p*p <= n:
            if is_prime[p]:
                for multiple in range(p*p, n, p):
                    is_prime[multiple] = False
            
            p += 1
        
        primes = [i for i, val in enumerate(is_prime) if val == True]
        return len(primes)