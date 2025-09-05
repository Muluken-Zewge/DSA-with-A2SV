# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        # Union indices from pairs
        for a, b in pairs:
            uf.union(a, b)

        # Group indices by root
        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        res = list(s)
        for indices in groups.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()
            for idx, ch in zip(indices, chars):
                res[idx] = ch

        return "".join(res)