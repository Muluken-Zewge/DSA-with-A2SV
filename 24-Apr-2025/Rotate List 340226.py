# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #handle edge cases(empty list, only one node, or no rotation(k=0))
        if not head or not head.next or k == 0:
            return head

        curr = head
        size = 0
        while curr.next:
            size += 1
            curr = curr.next
        old_tail = curr
        size += 1 #since we didn't count the last node to get the old tail

        k = k % size #to avoid unneccesary rotation if k > size
        if k == 0:
            return head
            
        #find the new tail
        new_tail = head
        for _ in range(size - k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        old_tail.next = head

        return new_head