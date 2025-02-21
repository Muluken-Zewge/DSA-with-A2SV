# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        answer = [0] * 2
        occurances = defaultdict(int) #store number of occurances of each element

        for num in nums:
            occurances[num] += 1
        
        for value in occurances.values():
            answer[0] += value // 2
            answer[1] += value % 2

        return answer         