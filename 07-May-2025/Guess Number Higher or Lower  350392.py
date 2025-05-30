# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low , high = 0, n
        while low <= high:
            mid = (low + high)//2
            if guess(mid) == 1:
                low = mid + 1
            elif guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 0:
                return mid