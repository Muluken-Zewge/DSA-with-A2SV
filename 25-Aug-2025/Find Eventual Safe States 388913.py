# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse = defaultdict(list)
        outdegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                reverse[v].append(u)
            outdegree[u] = len(graph[u])

        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            for prev in reverse[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    queue.append(prev)

        return [i for i in range(n) if safe[i]]
