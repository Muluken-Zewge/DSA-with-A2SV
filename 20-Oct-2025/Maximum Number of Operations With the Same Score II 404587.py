# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(l, r, target):
            if l >= r:
                return 0
            best = 0
            if nums[l] + nums[l+1] == target:
                best = max(best, 1 + dfs(l+2, r, target))
            if nums[r] + nums[r-1] == target:
                best = max(best, 1 + dfs(l, r-2, target))
            if nums[l] + nums[r] == target:
                best = max(best, 1 + dfs(l+1, r-1, target))
            return best

        ans = 0
        if n < 2:
            return 0

        # Try all possible initial moves (3 possibilities)
        ans = max(
            dfs(2, n-1, nums[0] + nums[1]) + 1,
            dfs(0, n-3, nums[-1] + nums[-2]) + 1,
            dfs(1, n-2, nums[0] + nums[-1]) + 1,
        )

        return ans
