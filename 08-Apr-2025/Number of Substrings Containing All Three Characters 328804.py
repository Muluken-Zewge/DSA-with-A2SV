# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        chars = {'a':1, 'b':1, 'c':1}
        s_map = defaultdict(int)
        left = 0
        num_of_sub_string = 0
        for right in range(len(s)):
            s_map[s[right]] += 1
            #while All(s_map[char] > 0 for char in 'abc')
            while chars['a'] <= s_map['a'] and chars['b'] <= s_map['b'] and chars['c'] <= s_map['c']:
                num_of_sub_string += len(s) - right
                s_map[s[left]] -= 1
                left += 1
            
                
        return num_of_sub_string