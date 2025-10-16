# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        pq = [(0, 0, 0)]  # (effort, r, c)
        
        while pq:
            eff, r, c = heapq.heappop(pq)
            if r == rows - 1 and c == cols - 1:
                return eff
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_eff = max(eff, abs(heights[nr][nc] - heights[r][c]))
                    if new_eff < effort[nr][nc]:
                        effort[nr][nc] = new_eff
                        heapq.heappush(pq, (new_eff, nr, nc))
        return -1
