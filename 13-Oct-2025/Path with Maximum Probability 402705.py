# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        # Build adjacency list
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        # Max-heap (store as negative to use min-heap as max-heap)
        heap = [(-1.0, start_node)]
        probs = [0.0] * n
        probs[start_node] = 1.0

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob

            # Early stop if we reached the end
            if node == end_node:
                return prob

            # Traverse neighbors
            for nei, edgeProb in graph[node]:
                newProb = prob * edgeProb
                if newProb > probs[nei]:
                    probs[nei] = newProb
                    heapq.heappush(heap, (-newProb, nei))

        return 0.0

        