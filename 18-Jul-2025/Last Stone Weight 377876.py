# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            big = -heapq.heappop(stones) 
            second_big = -heapq.heappop(stones) 
            if big != second_big:
                heapq.heappush(stones, -(big - second_big))
        
        return -stones[0] if stones else 0