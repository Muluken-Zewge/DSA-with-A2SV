# Problem: Recursive function to check if a string is palindrome - https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

# a function to check if the first and last char are the same
def isPalindromeHelper(s, left, right):
    #handles even length, odd lengh and empty strings
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindromeHelper(s, left + 1, right - 1)
    
def isPalindrom(s):
    n = len(s)
    return isPalindromeHelper(s, 0, n-1)