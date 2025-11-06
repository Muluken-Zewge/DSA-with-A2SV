# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # convert obstacles to a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        
        # directions: North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx = 0  # start facing north
        
        x = y = 0 # starting points
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:
                dir_idx = (dir_idx + 1) % 4  # turn right
            elif cmd == -2:
                dir_idx = (dir_idx - 1) % 4  # turn left
            else:
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x*x + y*y)
                    
        return max_dist
