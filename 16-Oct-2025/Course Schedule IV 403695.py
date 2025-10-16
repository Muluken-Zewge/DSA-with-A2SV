# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        prereq_sets = [set() for _ in range(numCourses)]

        # Build graph
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        # Topological sort
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            course = q.popleft()
            for nxt in graph[course]:
                # Add all prerequisites of course + course itself
                prereq_sets[nxt].add(course)
                prereq_sets[nxt] |= prereq_sets[course]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # Answer queries
        return [u in prereq_sets[v] for u, v in queries]
