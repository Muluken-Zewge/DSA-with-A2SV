# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #use dfs coloring
        n = len(graph)
        color = [-1 for _ in range(n)]#-1 means uncolored nodes

        def dfs(node, graph):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    if not dfs(neighbour,graph):
                        return False
                elif color[node] == color[neighbour]:
                    return False
            
            return True

        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node, graph):
                    return False

        return True

        