# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort() #sort the list
        min_idx = 0
        max_idx = len(piles) - 1
        max_coins = 0
#in each iteration, a triplet with the two largest elements and one smallest element is formed. 
#add the middle number(the second largest) in to the max_coins in each iteration
        for _ in range(len(piles)//3):
            max_coins += piles[max_idx-1]
            min_idx += 1
            max_idx -= 2
        
        return max_coins