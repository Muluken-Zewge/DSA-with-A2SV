# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        # Collect coordinates of 1s in both images
        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        # Count translation vectors
        shift_count = defaultdict(int)
        max_overlap = 0

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                dx = x2 - x1
                dy = y2 - y1
                shift_count[(dx, dy)] += 1
                max_overlap = max(max_overlap, shift_count[(dx, dy)])

        return max_overlap

        