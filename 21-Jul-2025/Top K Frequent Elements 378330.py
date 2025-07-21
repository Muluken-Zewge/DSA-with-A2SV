# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num in counter:
            frequency = counter[num]
            heappush(heap, (frequency, num))
            
            if len(heap) > k:
                heappop(heap)
        ans = [heap[i][1] for i in range(len(heap))]
        
        return ans