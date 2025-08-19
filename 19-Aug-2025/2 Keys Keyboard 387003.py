# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i   # worst case (all pastes)
            for j in range(i // 2, 1, -1):  # check divisors
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break   # smallest divisor gives best answer
        return dp[n]