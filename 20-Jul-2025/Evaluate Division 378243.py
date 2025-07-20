# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        def dfs(  left , right ,visited):
            if right  not in graph or left not in graph:
                return -1.0
            if right == left :
                return 1.0
            if left in graph:
                for neighbor, weight in graph[left]:
                    if right == neighbor:
                        return weight

            for neighbor, weight in graph[left]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor,right, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0

        n = len(values)
        for i in range(n):
            a, b = equations[i]
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1 / val)) 

        output = []        
        for query in queries:
            visited=set()
            left,right= query
            output.append(dfs(left, right , visited))

        return output