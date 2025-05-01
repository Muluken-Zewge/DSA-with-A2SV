# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size < self.k:
            new_node = ListNode(value)
            new_node.next = self.dummy_tail
            new_node.prev = self.dummy_tail.prev
            last_item = self.dummy_tail.prev
            last_item.next = new_node
            self.dummy_tail.prev = new_node
            self.size += 1

            return True
        
        return False

    def deQueue(self) -> bool:
        if self.size > 0:
            second_item = self.dummy_head.next.next
            self.dummy_head.next = second_item #make the head point the second item(now to become first)
            second_item.prev = self.dummy_head #make the second item the first
            self.size -= 1
        
            return True
    
        return False

    def Front(self) -> int:
        if self.size > 0:
            first_item = self.dummy_head.next
            return first_item.val
        else:
            return -1

    def Rear(self) -> int:
        if self.size > 0:
            last_item = self.dummy_tail.prev
            return last_item.val
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()