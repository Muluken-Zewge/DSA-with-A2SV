# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)
        for _ in range(k):
            big = -heappop(piles)
            remainig = ceil(big / 2)
            heappush(piles,-remainig)
        
        return -sum(piles)
