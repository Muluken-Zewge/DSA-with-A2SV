# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        pair_sum_count = defaultdict(int)
        total = 0

        # count all sum of pairs from nums1 and nums 2
        for a in range(n):
            for b in range(n):
                pair_sum_count[nums1[a]+nums2[b]] += 1
        
        # check sum of pairs from nums3 and nums4 that can cancel them
        for c in range(n):
            for d in range(n):
                current_sum = nums3[c] + nums4[d]
                complement = 0 - current_sum
                if complement in pair_sum_count:
                    total += pair_sum_count[complement]

        return total
