# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(n):
            if n == 1:
                return False
            d = 2
            while d * d <= n:
                if n % d == 0:
                    return False
                d += 1
            return True
        def is_palindrome(n):
            s = str(n)
            return s == s[::-1]

        while True:
            if len(str(n)) % 2 == 0 and n > 11:
                n = 10 ** len(str(n))
                continue
            if is_prime(n) and is_palindrome(n):
                return n
            n += 1