# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        dummy1 = ListNode() # for the smaller partition
        dummy2 = ListNode() # for the larger partition
        curr1 , curr2 = dummy1, dummy2
        while curr:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr
            else:
                curr2.next = curr
                curr2 = curr
            curr = curr.next

        curr2.next = None # cut the link for the last element of the larger partition since it'll be the last node(unless there will be a loop)
        curr1.next = dummy2.next # connect the two nodes

        return dummy1.next