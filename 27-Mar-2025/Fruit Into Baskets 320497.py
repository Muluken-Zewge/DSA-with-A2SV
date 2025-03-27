# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        max_fruits = 0
        
        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            
            # Shrink the window if more than 2 types of fruits are in the basket
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            
            # Update the maximum fruits collected
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits