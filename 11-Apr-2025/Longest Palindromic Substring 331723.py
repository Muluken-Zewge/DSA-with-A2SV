# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #expand around the center approach
        def expand(left: int, right: int) -> str:#helper function to expand
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]
        
        longest = ''
        for i in range(len(s)):
            odd_length = expand(i,i)
            if len(odd_length) > len(longest):
                longest = odd_length
            even_length = expand(i, i+1)
            if len(even_length) > len(longest):
                longest = even_length

        return longest
