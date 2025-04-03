# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pairs = 0
        pairs_dict = defaultdict(int)
        left = 0
        good_sub_arrays = 0

        for right in range(len(nums)):
            # Add current number and update pairs
            pairs += pairs_dict[nums[right]]
            pairs_dict[nums[right]] += 1 

            # Shrink left pointer if we have enough pairs
            while pairs >= k:
                # Count subarrays ending at `right`
                good_sub_arrays += len(nums) - right 
                # Remove `nums[left]` effect from pairs 
                pairs -= pairs_dict[nums[left]] - 1  
                # Decrease count of `nums[left]`
                pairs_dict[nums[left]] -= 1  
                left += 1

        return good_sub_arrays