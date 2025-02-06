# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #check if the two strings are equal
        if s1 == s2:
            output = True
        else:
            #to store indexes where characters aren't equal
            different_charaters = [] 
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    different_charaters.append(i)
            #check if the number of diferent chars is not 2
            if len(different_charaters) != 2:
                output = False
            else:
                i,j = different_charaters
                #check if the two chars are the same set of characters
                if s1[i] == s2[j] and s1[j] == s2[i]:
                    output = True
                else:
                    output = False
            
        return output