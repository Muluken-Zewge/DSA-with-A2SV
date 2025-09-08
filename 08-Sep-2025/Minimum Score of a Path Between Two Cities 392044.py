# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set()
        q = deque([1])
        visited.add(1)

        min_score = float("inf")
        while q:
            node = q.popleft()
            for nei, d in graph[node]:
                min_score = min(min_score, d)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return min_score