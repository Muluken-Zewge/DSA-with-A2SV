# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_window = set() #to check for duplicates
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in current_window:
                current_window.remove(s[left])
                left += 1
            current_window.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
