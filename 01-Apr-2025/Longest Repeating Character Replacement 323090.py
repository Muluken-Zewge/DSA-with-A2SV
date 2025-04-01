# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        freq_map = {}  # To count character frequencies in the window
        max_freq = 0  # Most frequent character count in the current window

        for right in range(len(s)):
            char = s[right]
            freq_map[char] = freq_map.get(char, 0) + 1
            max_freq = max(max_freq, freq_map[char])

        # If the number of replacements needed exceeds `k`, shrink the window
            while (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1  # Shrink the window
            
            longest = max(longest, right - left + 1)

        return longest