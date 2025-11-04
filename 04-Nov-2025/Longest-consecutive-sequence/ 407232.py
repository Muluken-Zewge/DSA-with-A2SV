# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0
        for num in num_set:
            # check if the number can be a start to a sequence
            if (num - 1) not in num_set:
                curr = num
                length = 1
                while curr + 1 in num_set:
                    length += 1
                    curr += 1
                longest_sequence = max(longest_sequence, length)
        
        return longest_sequence