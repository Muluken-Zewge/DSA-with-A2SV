# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
    
        #a function to check if all the balls can be palced with in the passed distance
        def can_position(distance):
            last_placed_position = position[0]
            ball_count = 1
            for i in range(1, len(position)):
                if position[i] - last_placed_position >= distance:
                    ball_count += 1
                    last_placed_position = position[i]
            
            return ball_count >= m
        
        #binary search for maximixing the distance(force)
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right)//2
            if can_position(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right