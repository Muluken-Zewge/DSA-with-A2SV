# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

#use bianry search of 'search on output space' variant
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #function to check if 'k' is valid
        def is_k_valid(k):
            hours = 0
            for pile in piles:
                if pile % k == 0:
                    hours += (pile//k)
                else:
                    hours += (pile//k) + 1

            return hours <= h

        #binary search to minimize k
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right)//2
            if is_k_valid(mid):
                right = mid
            else:
                left = mid + 1

        return left