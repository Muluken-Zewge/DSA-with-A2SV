# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        uf = UnionFind()
        OFFSET = 10001  # offset for column index

        for x, y in stones:
            uf.union(x, y + OFFSET)

        roots = {uf.find(x) for x, y in stones for x in (x, y + OFFSET)}
        return len(stones) - len(roots)
