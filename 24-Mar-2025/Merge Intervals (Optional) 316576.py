# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the intervals based on the start value
        intervals.sort()
        
        merged = []
        current_interval = intervals[0]
        
        for interval in intervals[1:]:
        # If the current interval overlaps with the next interval, merge them
            if interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], interval[1])
            else:
            # If they don't overlap, add the current interval to the merged list
                merged.append(current_interval)
                current_interval = interval
        
        # Add the last interval
        merged.append(current_interval)
        
        return merged