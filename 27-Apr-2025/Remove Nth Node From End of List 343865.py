# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        head = dummy
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        needed = size - n
        curr = head
        for _ in range(needed - 1):
            curr = curr.next
        curr.next = curr.next.next

        return dummy.next