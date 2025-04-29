# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #approach1: two-pointer method, by reversing the second half of the list

        #step1:find the middle node to reverse
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #step2: reverse the second half as new linked list
        newListHead = slow
        prev = None
        while newListHead:
            NewListcurr = ListNode(newListHead.val)
            NewListcurr.next = prev
            prev = NewListcurr
            newListHead = newListHead.next

        #step3: find max_twin_sum
        reversedHead = prev
        originalHead = head
        max_twin_sum = float(-inf)
        while reversedHead:
            max_twin_sum = max(max_twin_sum, reversedHead.val + originalHead.val)
            reversedHead = reversedHead.next
            originalHead = originalHead.next
        
        return max_twin_sum

        #approach2: using a list
        # stack = []
        # max_twin_sum = float(-inf)
        # curr = head
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        # left , right = 0, len(stack) - 1
        # while left < right:
        #     max_twin_sum = max(max_twin_sum, stack[left] + stack[right])
        #     left += 1
        #     right -= 1

        # return max_twin_sum