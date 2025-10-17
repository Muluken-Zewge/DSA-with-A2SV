# Problem: Minimum Weighted Subgraph With the Required Paths - https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        MOD = 10**9 + 7

        # Build adjacency list for both original and reverse graph
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))
        
        def dijkstra(start, graph):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in graph[node]:
                    nd = d + w
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(pq, (nd, nei))
            return dist

        # Run Dijkstra from src1, src2, and dest (on reversed graph)
        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        dist3 = dijkstra(dest, rev_graph)

        ans = float('inf')
        for v in range(n):
            if dist1[v] != float('inf') and dist2[v] != float('inf') and dist3[v] != float('inf'):
                ans = min(ans, dist1[v] + dist2[v] + dist3[v])

        return ans if ans != float('inf') else -1

        