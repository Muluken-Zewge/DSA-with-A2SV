# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left , right = 0, len(people) - 1
        boat = 0

        while left <= right:
            if people[right] + people[left] > limit:
                boat += 1
                right -= 1
            else:
                boat += 1
                left += 1
                right -= 1
        
        return boat