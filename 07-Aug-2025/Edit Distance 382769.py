# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create DP table of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i  # word1 to empty: delete all
        for j in range(n + 1):
            dp[0][j] = j  # empty to word2: insert all

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )

        return dp[m][n]