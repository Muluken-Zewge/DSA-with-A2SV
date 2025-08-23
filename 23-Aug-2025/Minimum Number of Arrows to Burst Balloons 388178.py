# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0


        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])


        arrows = 1
        pos = points[0][1]


        for start, end in points:
            if start > pos:
                arrows += 1
                pos = end


        return arrows