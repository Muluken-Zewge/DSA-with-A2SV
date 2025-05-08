# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left , right = 0, len(letters)-1
        index = 0
        while left <= right:
            mid = (left + right)//2
            # if mid > target, check all elements before mid to find the first greater
            if letters[mid] > target:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return letters[index]