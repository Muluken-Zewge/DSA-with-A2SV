# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)

        return provinces
