# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        consistent_strings = 0
        for word in words:
            is_consistent = True #assume the string is consitent
            for char in word:
                #make the string inconsitent if a char isnot in allowed
                if char not in allowed:
                    is_consistent = False
                    break
            #increment 1 to consistent_strings 
            if is_consistent:
                consistent_strings += 1

        return consistent_strings