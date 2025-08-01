# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        # Push first element of each row (only first column)
        for r in range(min(n, k)):
            heappush(min_heap, (matrix[r][0], r, 0))

        # Extract min k times
        while k > 0:
            val, r, c = heappop(min_heap)
            if c + 1 < n:
                heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            k -= 1

        return val