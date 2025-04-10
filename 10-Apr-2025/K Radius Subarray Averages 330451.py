# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [0] * n
        prefix_sum = [0] * (n + 1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        for i in range(n):
            if (i - k >= 0) and (i + k < n):
                sum_ = prefix_sum[i+k+1] - prefix_sum[i-k]
                avg = sum_ // (2*k + 1)
                avgs[i] = avg
            else:
                avgs[i] = -1

        return avgs