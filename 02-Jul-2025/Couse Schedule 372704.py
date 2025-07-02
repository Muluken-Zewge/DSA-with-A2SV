# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for ai,bi in prerequisites:
            graph[bi].append(ai)
        
        colors = [-1 for _ in range(numCourses)]
        #-1 represent white(unvisited)
        # 0 represent grey(visited but not exited it's path yet)
        # 1 represent black(visited and exited it's path)
        
        is_possible = True

        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return
            colors[node] = 0

            for neighbour in graph[node]:
                #if it is invisited, run dfs on it
                if colors[neighbour] == -1:
                    dfs(neighbour)
                #if the neighbour and node are both colored 0,we find the node in it's own path which indicate a cycle exists
                elif colors[neighbour] == 0:
                    is_possible = False

            colors[node] = 1 #color it black when existing the path
        
        #run for loop over all courses to check disconnected graphs
        for course in range(numCourses):
            if colors[course] == -1:
                dfs(course)

        return is_possible

        