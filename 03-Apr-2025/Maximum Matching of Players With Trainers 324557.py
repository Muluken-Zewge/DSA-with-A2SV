# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p = 0 # player pointer
        t = 0 # trainer pointer
        max_match = 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                max_match += 1
                p += 1
                t += 1
            else:
                t += 1
        
        return max_match