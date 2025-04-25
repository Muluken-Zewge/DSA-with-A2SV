# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.requests = 0
        self.request_queue = deque()

    def ping(self, t: int) -> int:
        if not self.request_queue:
            self.request_queue.append(t)
            return 1

        while self.request_queue and t - self.request_queue[0] > 3000 :
            self.request_queue.popleft()
        self.request_queue.append(t)
        
        requests = len(self.request_queue)

        return requests

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)