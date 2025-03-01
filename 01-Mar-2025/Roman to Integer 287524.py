# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        mapper= { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        integer = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and mapper[s[i]] < mapper[s[i+1]]:
                integer -= mapper[s[i]]
            else:
                integer += mapper[s[i]]

        return integer