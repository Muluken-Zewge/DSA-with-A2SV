# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        for i in range(len(s)):
            if s_counter[s[i]] == 1:
                return i
        
        return -1