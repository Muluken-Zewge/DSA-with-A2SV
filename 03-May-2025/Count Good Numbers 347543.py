# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        #function to calculate power of a number
        def myPow(x,n):
            if n == 0:
                return 1
            if n % 2 == 0:
                half = myPow(x, n//2) % MOD
                return half * half
            else:
                return x * myPow(x, n-1) % MOD
        
        return myPow(5,(n+1)//2) % MOD * myPow(4, n//2) % MOD