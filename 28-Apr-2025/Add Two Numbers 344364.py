# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy1.next = l1
        l1 = dummy1

        p1 , p2 = dummy1.next, l2 #pointers for adding nodes
        prev1 = dummy1 #pointer to track the last element of l1
        rem = 0 #a variable to store the remainder
        while p1 and p2:
            p1.val = p1.val + p2.val + rem
            rem = 0
            if p1.val >= 10:
                p1.val = p1.val % 10
                rem = 1
            p1, p2 = p1.next, p2.next
            prev1 = prev1.next

        #if p2 is smaller
        while p1:
            p1.val = p1.val + rem
            if p1.val >= 10:
                p1.val = p1.val % 10
                rem = 1
            else:
                rem = 0
            p1 = p1.next
            prev1 = prev1.next
        #if p1 is smaller
        while p2:
            val = p2.val + rem
            if val >= 10:
                val = val % 10
                rem = 1
            else:
                rem = 0
            prev1.next = ListNode(val)
            p2 = p2.next
            prev1 = prev1.next
        #if the last sum is >= 10
        if rem == 1:
            prev1.next = ListNode(rem)

        return dummy1.next