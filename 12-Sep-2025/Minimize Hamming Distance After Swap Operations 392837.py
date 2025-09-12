# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

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
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for a, b in allowedSwaps:
            uf.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        distance = 0
        for indices in groups.values():
            count_source = Counter(source[i] for i in indices)
            count_target = Counter(target[i] for i in indices)
            # Compute mismatches
            for val, freq in (count_target - count_source).items():
                distance += freq

        return distance
        