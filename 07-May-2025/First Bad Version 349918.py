# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low , high = 1, n
        while low < high:# the loop terminates when low == high(low have the answer at that point)
            mid = (low + high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low
# the low will stop at the first bad and high will move to the left untill it's equal with low since mid will always be less than high

            