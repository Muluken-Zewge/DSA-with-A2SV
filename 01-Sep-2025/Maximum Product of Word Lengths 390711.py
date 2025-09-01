# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words):
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        # Build mask and store length
        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask
            lengths[i] = len(word)

        # Check all pairs
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:  # no common letter
                    ans = max(ans, lengths[i] * lengths[j])

        return ans
