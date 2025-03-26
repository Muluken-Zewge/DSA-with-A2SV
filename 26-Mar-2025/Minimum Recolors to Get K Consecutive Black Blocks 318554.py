# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        required_block = 'B' * k
        if required_block in blocks:
            return 0
        
        min_operation = float("inf")

        for left in range(len(blocks) - k + 1):
            current_window_count = 0
            right = left 
            while right - left + 1 <= k:
                if blocks[right] == 'W':
                    current_window_count += 1
                right += 1
            min_operation = min(min_operation, current_window_count)
        
        return min_operation