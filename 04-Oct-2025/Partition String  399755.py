# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        res = []
        i = 0
        n = len(s)

        while i < n:
            curr = ""
            j = i
            while j < n:
                curr += s[j]
                if curr not in seen:
                    seen.add(curr)
                    res.append(curr)
                    break
                j += 1
            i = j + 1
        return res
