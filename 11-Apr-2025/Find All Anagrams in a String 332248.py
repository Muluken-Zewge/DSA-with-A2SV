# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = defaultdict(int)
        for char in p:
            p_count[char] += 1

        s_count = defaultdict(int)
        output = []
        left = 0

        for right in range(len(s)):
            s_count[s[right]] += 1

            # Ensure window size is same as p
            if right - left + 1 > len(p):
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1

            # Compare dicts
            if s_count == p_count:
                output.append(left)

        return output