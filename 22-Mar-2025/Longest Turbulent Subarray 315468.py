# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        answer = 1
        left = 0

        for right in range(1, n):
            if arr[right] > arr[right - 1]:
                cur_dir = 1  # up
            elif arr[right] < arr[right - 1]:
                cur_dir = -1  # down
            else:
                cur_dir = 0  # equal
            
            if cur_dir == 0:
                left = right
                continue
            if right > left + 1: # window size is > 2
                if arr[right - 1] > arr[right - 2]:
                    prev_dir = 1 # up
                elif arr[right - 1] < arr[right - 2]:
                    prev_dir = -1 # down
                else:
                    prev_dir = 0 # same
                
                if prev_dir == cur_dir or prev_dir == 0:
                    left = right - 1

            cur_window = right - left + 1
            answer = max(answer, cur_window)

        return answer