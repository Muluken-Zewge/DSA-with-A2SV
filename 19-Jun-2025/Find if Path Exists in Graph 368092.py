# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #construct the graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set() #to track visited nodes to avoid infinite loop
        
        def dfs(node, visited):
            #base case
            if node == destination:
                return True
            
            visited.add(node)
            #check all paths
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                    if found:
                        return True
            
            return False
        
        return dfs(source, visited)