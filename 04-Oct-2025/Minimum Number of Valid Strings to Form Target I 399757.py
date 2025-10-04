# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False  # not needed, but kept for clarity

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        # Build Trie from words (store all prefixes)
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
        
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0

        # DP from right to left
        for i in range(n - 1, -1, -1):
            node = root
            for j in range(i, n):
                if target[j] not in node.children:
                    break
                node = node.children[target[j]]
                # Every prefix match counts (not just full words)
                dp[i] = min(dp[i], 1 + dp[j + 1])
        
        return dp[0] if dp[0] != float('inf') else -1
 