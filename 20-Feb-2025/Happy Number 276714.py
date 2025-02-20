# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set() #to chack if the number cyles
        
        while n != 1:
            #return false if cyles
            if n in cycle:
                return False
            
            #if not in cycle, add n in cycle and update to sum of its digits
            cycle.add(n) 
            n = sum(int(num)**2 for num in str(n))
        
        return True