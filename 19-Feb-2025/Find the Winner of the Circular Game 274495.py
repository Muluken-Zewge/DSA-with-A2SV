# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        starting_position = 0

        while n > 1:
            loser_index = (starting_position + k - 1) % n
            friends.pop(loser_index)
            starting_position = loser_index
            n -= 1
        
        return friends[0]