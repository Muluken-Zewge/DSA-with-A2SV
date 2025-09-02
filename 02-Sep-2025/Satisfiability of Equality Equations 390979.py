# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]

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
    def equationsPossible(self, equations: list[str]) -> bool:
        uf = UnionFind()

        # First pass: handle "=="
        for eq in equations:
            if eq[1:3] == "==":
                uf.union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))

        # Second pass: handle "!="
        for eq in equations:
            if eq[1:3] == "!=":
                if uf.find(ord(eq[0]) - ord('a')) == uf.find(ord(eq[3]) - ord('a')):
                    return False

        return True
        