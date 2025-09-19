# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a: int, b: int):
            if b == 0:
                return a
            return gcd(b, a % b)
        smallest = min(nums)
        largest = max(nums)

        return gcd(smallest, largest)