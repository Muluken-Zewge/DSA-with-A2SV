# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_position = [0,0]
        is_possible = True #assume it is possibe to escape
        for ghost in ghosts:
            #calculate the distance b/n a ghost and a target
            ghost_target_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            #calculate the distnace b/n my position and a ghost
            my_Position_target_distnace = abs(my_position[0] - target[0]) + abs(my_position[1] - target[1])

            if  my_Position_target_distnace >= ghost_target_distance:
                is_possible = False
                break
                
        return is_possible
        