# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        seen_s = set()
        seen_t = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in seen_t:
                    return False

                mapping[s[i]] = t[i]
                seen_s.add(s[i])
                seen_t.add(t[i])
        
        return True