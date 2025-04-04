# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ps = 0 # s-pointer
        pt = 0 # t-pointer
        while ps < len(s) and pt < len(t):
            if t[pt] == s[ps]:
                ps += 1
                pt += 1
            else:
                ps += 1
        
        return len(t) - pt