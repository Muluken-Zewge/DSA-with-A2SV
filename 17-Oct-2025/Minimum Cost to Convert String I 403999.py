# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        INF = float('inf')
        n = 26  # lowercase letters
        dist = [[INF] * n for _ in range(n)]

        # self to self cost = 0
        for i in range(n):
            dist[i][i] = 0

        # build graph
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - 97, ord(c) - 97
            dist[u][v] = min(dist[u][v], w)  # pick cheapest edge if duplicates exist

        # Floyd–Warshall all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u, v = ord(s) - 97, ord(t) - 97
            if dist[u][v] == INF:
                return -1  # impossible transformation
            total_cost += dist[u][v]

        return total_cost        