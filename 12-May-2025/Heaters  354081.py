# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def can_cover(radius):
            for house in houses:
                #find the closest heater for in the heaters array
                idx = bisect_left(heaters,house)

                #distance to closest heater on the left and right
                if idx == 0:
                    left_dist = float('inf')
                else:
                    left_dist = abs(house - heaters[idx - 1])
                
                if idx == len(heaters):
                    right_dist = float('inf')
                else:
                    right_dist = abs(heaters[idx] - house)

            # If nearest heater is farther than radius, house is not covered
                if min(left_dist, right_dist) > radius:
                    return False

            return True

        left, right = 0, 10**9
        while left < right:
            mid = (left + right)//2
            if can_cover(mid):
                right = mid
            else:
                left = mid + 1
        
        return left