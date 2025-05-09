# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left , right = 0, n
        while left <= right:
            mid = (left + right)//2
            total = mid*(mid+1)//2
            if total > n:
                right = mid - 1
            elif total < n:
                left = mid + 1
            else:
                return mid
        
        return right
