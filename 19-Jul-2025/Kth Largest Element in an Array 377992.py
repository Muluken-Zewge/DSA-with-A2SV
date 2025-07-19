# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # we push nums to heap untill it its lenght exceeds k, then pop
        # when for loop terminates, kth largest element will be on the root
        for num in nums:
            heappush(heap,num)
            if len(heap) > k:
                heappop(heap)
        
        return heap[0]