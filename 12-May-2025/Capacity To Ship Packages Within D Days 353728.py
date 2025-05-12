# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
        #Check if we can ship all packages within 'days' given this capacity
            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    # Exceeds capacity, start a new day
                    days_needed += 1
                    current_load = 0
                current_load += weight

            return days_needed <= days

        # Binary search range: [max_weight, sum_of_weights]
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid  # Try smaller capacity
            else:
                left = mid + 1  # Need more capacity

        return left  # Minimum valid capacity