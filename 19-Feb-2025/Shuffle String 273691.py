# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str = [0] * len(s)
        for i in range(len(s)):
            str[indices[i]] = s[i]
        
        return "".join(str)