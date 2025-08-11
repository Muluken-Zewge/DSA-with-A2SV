# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case: one way to make 0

        # Loop coins first to avoid counting permutations
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]

        return dp[amount]