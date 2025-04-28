# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #check if the list is empty or has only one node
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        head = dummy
        left = dummy.next
        right = left.next
        while right:
            if left.val == right.val:
                left.next = right.next
            else:
                left = left.next
            right = right.next

        return dummy.next