# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        min_time = 0
        i = 0
        j = 0
        while i < len(processorTime) and j < len(tasks):
                min_time = max(min_time, processorTime[i]+tasks[j])
                i += 1
                j += 4

        return min_time