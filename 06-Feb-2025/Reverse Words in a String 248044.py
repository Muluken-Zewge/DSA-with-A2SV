# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #convert the string to list of strings 
        list_of_strings = s.strip().split()
        list_of_strings.reverse()

        #join the strings with a space in beteween
        reversed_string = " ".join(list_of_strings)
        return reversed_string