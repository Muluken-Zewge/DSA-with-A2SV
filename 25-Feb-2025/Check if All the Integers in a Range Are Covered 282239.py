# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        interval = set()
        for n in ranges:
            interval.update(range(n[0], n[1]+1))
        
        for num in range(left, right + 1):
            if num not in interval:
                return False
        
        return True