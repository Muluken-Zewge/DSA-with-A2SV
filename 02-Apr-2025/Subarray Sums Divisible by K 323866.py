# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        num_of_sub_array = 0
        remainder_count = defaultdict(int)
        # Initialize for cases where prefix sum itself is divisible by k
        remainder_count[0] = 1  

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # If the remainder appeared before, add its count to result
            num_of_sub_array += remainder_count[remainder]

            # Update count of this remainder
            remainder_count[remainder] += 1

        return num_of_sub_array