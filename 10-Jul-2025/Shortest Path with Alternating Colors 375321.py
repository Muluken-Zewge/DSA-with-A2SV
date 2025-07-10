# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        dist = [-1] * n

        #BFS with (node, step_count, last_color)
        queue = deque()
        visited = set()

        #Start from node 0 with both red and blue
        queue.append((0, 0, None))  # None = no color yet
        visited.add((0, None))

        while queue:
            node, steps, last_color = queue.popleft()

            # First time visiting a node = shortest path
            if dist[node] == -1:
                dist[node] = steps

            # Determine next color to use
            if last_color != 'red':  # Try red next
                for nei in red_graph[node]:
                    if (nei, 'red') not in visited:
                        visited.add((nei, 'red'))
                        queue.append((nei, steps + 1, 'red'))

            if last_color != 'blue':  # Try blue next
                for nei in blue_graph[node]:
                    if (nei, 'blue') not in visited:
                        visited.add((nei, 'blue'))
                        queue.append((nei, steps + 1, 'blue'))

        return dist
        