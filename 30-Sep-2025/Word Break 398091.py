# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)   # faster lookups
        n = len(s)

        # dp[i] = True if s[:i] can be segmented into words from the dict
        dp = [False] * (n + 1)
        dp[0] = True   # empty string is always segmentable

        # build up dp
        for i in range(1, n + 1):       # endpoint of substring
            for j in range(i):          # cut position
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break               # no need to check further cuts

        return dp[n]