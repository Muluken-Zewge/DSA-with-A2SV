# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        rights = [interval[0] for interval in intervals]
        rights.sort()
        pairs = {}
        ans = []
        for i,interval in enumerate(intervals):
            pairs[interval[0]] = i
        for interval in intervals:
            bisected = bisect_left(rights, interval[1])
            if bisected >= len(rights):
                ans.append(-1)
            else:
                num = rights[bisected]
                ans.append(pairs[num])
        
        return ans
