# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left , right = 0, len(skill) - 1
        standard = skill[left] + skill[right]
        equal_skill = []
        while left < right:
            if skill[left] + skill[right] != standard:
                return -1
            else:
                equal_skill.append((skill[left], skill[right]))
            left += 1
            right -= 1
            
        chemistry = 0
        for team in equal_skill:
            chemistry += team[0] * team[1]
        
        return chemistry
        