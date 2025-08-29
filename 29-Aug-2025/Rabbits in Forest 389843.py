# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0
        for x, f in freq.items():
            group_size = x + 1
            groups = math.ceil(f / group_size)
            total += groups * group_size
        return total
