# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for pair in trust:
            graph[pair[0]].append(pair[1])
        if len(graph.keys()) + 1 != n:
            return -1
        for num in range(1,n+1):
            if num not in graph.keys():
                judge = num
        for vertices in graph.values():
            if judge not in vertices:
                return -1
        
        return judge