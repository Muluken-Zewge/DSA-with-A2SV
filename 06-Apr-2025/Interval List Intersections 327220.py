# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        ans = []
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]
            
            # Check if intervals overlap
            if start1 <= end2 and start2 <= end1:
                # Compute the intersection
                ans.append([max(start1, start2), min(end1, end2)])
            
            # Move the pointer with the smaller end time
            if end1 < end2:
                p1 += 1
            else:
                p2 += 1
                
        return ans
