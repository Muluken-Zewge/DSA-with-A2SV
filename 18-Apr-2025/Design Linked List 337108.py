# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node(0)  # dummy node to simplify edge cases
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new_node = Node(val)
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1