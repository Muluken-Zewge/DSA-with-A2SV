# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        size = 0
        ans = []
        #find the size of the linked list
        while curr:
            size += 1
            curr = curr.next

        # if k >= size, there will be empty arrays while all the non-empty ones has exactly one element
        temp = head
        if k >= size:
            while temp:
                ans.append(temp)
                nextTemp = temp.next
                temp.next = None
                temp = nextTemp
            for _ in range(k-size):
                ans.append(None)
            
            return ans
        
        num_of_node = size // k #number of element in each partition
        rem = size % k #remainder to be distributed for parts occuring earlier

        curr = head
        while curr:
            for _ in range(num_of_node - 1 + (1 if rem > 0 else 0)):
                curr = curr.next
            nextCurr = curr.next
            curr.next = None
            curr = nextCurr
            rem -= 1
            ans.append(head)

            head = nextCurr

        return ans