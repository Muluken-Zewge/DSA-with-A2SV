# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # collect all match positions for a and b
        A, B = [], []
        len_a, len_b = len(a), len(b)
        n = len(s)

        for i in range(n - len_a + 1):
            if s[i:i+len_a] == a:
                A.append(i)
        for j in range(n - len_b + 1):
            if s[j:j+len_b] == b:
                B.append(j)

        # two-pointer approach
        res = []
        j = 0
        for i in A:
            # Move j to the first possible b-index within range [i - k, i + k]
            while j < len(B) and B[j] < i - k:
                j += 1
            # Check if there's at least one valid b within distance k
            if j < len(B) and abs(B[j] - i) <= k:
                res.append(i)

        return res
