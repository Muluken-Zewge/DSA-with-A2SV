# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        #function to check if a string is a Palindrome
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        left , right = 0, len(s)-1
        while left <= right:
            #check if the chars tracked by the pointers are not the same
            if s[left] != s[right]:
                #create two strings removing the of the chars at a time 
                temp1 = s[:left] + s[left+1:]
                temp2 = s[:right] + s[right+1:]
                # if one of the strings is a palindrome,return True(s can be a palindrome by removing at most 1 char)
                return isPalindrome(temp1) or isPalindrome(temp2)
            left += 1
            right -= 1
        
        return True