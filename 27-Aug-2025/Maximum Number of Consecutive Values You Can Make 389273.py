# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_reachable = 0

        for c in coins:
            if c > max_reachable + 1:
                break
            max_reachable += c

        return max_reachable + 1
