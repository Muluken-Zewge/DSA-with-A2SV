# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        count = {}
        owners = {}  # track which string a substring belongs to

        # build substring frequency map
        for i, word in enumerate(arr):
            seen = set()
            for l in range(1, len(word) + 1):
                for start in range(len(word) - l + 1):
                    sub = word[start:start + l]
                    if sub not in seen:  # avoid duplicate substrings per word
                        seen.add(sub)
                        count[sub] = count.get(sub, 0) + 1
                        owners[sub] = i if count[sub] == 1 else -1  # -1 = shared

        # for each word, find unique substrings
        res = []
        for i, word in enumerate(arr):
            best = ""
            for l in range(1, len(word) + 1):
                candidates = []
                for start in range(len(word) - l + 1):
                    sub = word[start:start + l]
                    if count[sub] == 1 and owners[sub] == i:
                        candidates.append(sub)
                if candidates:
                    best = min(candidates)
                    break
            res.append(best)
        return res
