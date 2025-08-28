# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Attach index to each task
        indexed_tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        # Sort by enqueueTime
        indexed_tasks.sort()

        result = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            # Push all tasks that are now available
            while i < n and indexed_tasks[i][0] <= time:
                et, pt, idx = indexed_tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
            
            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                result.append(idx)
            else:
                # No available tasks, jump to the next task's enqueueTime
                time = indexed_tasks[i][0]

        return result
