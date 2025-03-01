# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        answer = []

        for num, occurance in nums_counter.items():
            if occurance == 2:
                answer.append(num)

        return answer
