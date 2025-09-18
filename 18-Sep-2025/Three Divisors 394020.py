# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        def is_prime(n):
            d = 2
            while d * d <= n:
                if n % d == 0:
                    return False
                d += 1
            return True
        # the square of a prime number has exactly 3 facors
        root = int(sqrt(n))
        if root * root != n or n == 1:
            return False
        
        return is_prime(root)