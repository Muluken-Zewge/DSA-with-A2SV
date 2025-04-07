# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s_list = []
        prefix = [0] * n

        for shift in shifts:
            l, r, d = shift
            if d == 1:
                prefix[l] += 1
                if r + 1 < n:
                    prefix[r+1] -= 1
            else:
                prefix[l] -= 1
                if r + 1 < n:
                    prefix[r+1] += 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] + prefix[i]

        for i in range(len(s)):
            new_char_ord = ((ord(s[i]) - ord('a')) + prefix[i]) % 26 + ord('a')
            new_char = chr(new_char_ord)
            s_list.append(new_char)

        return "".join(s_list)