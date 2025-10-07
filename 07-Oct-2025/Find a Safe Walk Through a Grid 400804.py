# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path




class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS queue: (row, col, remaining_health)
        q = deque([(0, 0, health - grid[0][0])])
        if q[0][2] <= 0:
            return False  # can't even start safely

        # Track best remaining health at each cell
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = q[0][2]

        while q:
            i, j, h = q.popleft()

            # Check if reached goal with health ≥ 1
            if i == m - 1 and j == n - 1 and h >= 1:
                return True

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_health = h - grid[ni][nj]
                    if new_health > 0 and new_health > visited[ni][nj]:
                        visited[ni][nj] = new_health
                        q.append((ni, nj, new_health))

        return False
