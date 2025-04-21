# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Find the middle (slow will point to the middle)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        #Compare the first and second halves
        left, right = head, prev
        while right:  # Only need to check right half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
