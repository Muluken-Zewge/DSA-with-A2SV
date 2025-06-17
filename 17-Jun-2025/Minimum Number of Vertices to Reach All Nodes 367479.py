# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans  = set()
        reachable = set()
        for vertices in edges:
            reachable.add(vertices[1])
        for vertices in edges:
            if vertices[0] not in reachable:
                ans.add(vertices[0])
        
        return list(ans)