# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count_at_most(k):
            checker = defaultdict(int)
            left = 0
            result = 0
            for right in range(len(nums)):
                checker[nums[right]] += 1
                while len(checker) > k:
                    checker[nums[left]] -= 1
                    if checker[nums[left]] == 0:
                        del checker[nums[left]]
                    left += 1
                
                result += right - left + 1
            
            return result

        return count_at_most(k) - count_at_most(k-1)
