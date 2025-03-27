# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        a = 0 #left pointer
        longest = 1
        adjacent_pairs = 0  

        for b in range(1, len(s)):  # Right pointer
            if s[b] == s[b - 1]:
                adjacent_pairs += 1
            
            while adjacent_pairs > 1: #shrink window if > 1 adjacent pair
                if s[a] == s[a + 1]:  
                    adjacent_pairs -= 1  # Remove the first adjacent pair
                a += 1  
            
            longest = max(longest, b - a + 1)  # Update max length
        
        return longest
