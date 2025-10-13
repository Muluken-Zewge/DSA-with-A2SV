# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Min-heap for Dijkstra
        min_heap = [(0, k)]  # (time, node)
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time

            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(min_heap, (time + wt, nei))
        
        # If not all nodes reached, return -1
        if len(dist) < n:
            return -1
        
        # Max time among all shortest paths
        return max(dist.values())
