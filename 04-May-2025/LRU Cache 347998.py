# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

# use doubly linked list and a dictionary for O(1) access. move elements added or modified to the top(head) as recently accesed while the least recently accessed movet to the tail
class ListNode:
    def __init__(self, val={}, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0
        self.cache = {}

    def move_to_front(self, node):
        # Disconnect the node
        node.prev.next = node.next
        node.next.prev = node.prev
        # Reconnect it right after dummy_head
        first_node = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = first_node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_front(node)
            return node.val[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            # modify the val and remove from that position
            node.val[key] = value
            self.move_to_front(node)
            
        else:
            # if the key doesn't exist, creat a new node and put it on top
            new_node = ListNode({key:value})
            self.cache[key] = new_node
            first_node = self.dummy_head.next
            new_node.next = first_node
            first_node.prev = new_node
            self.dummy_head.next = new_node
            new_node.prev = self.dummy_head
            self.size += 1
            #after adding the new node, if size > capacity, we remove the least recently accesses node(the one before the tail)
            if self.size > self.capacity:
                lru_node = self.dummy_tail.prev
                prev_node = lru_node.prev
                prev_node.next = self.dummy_tail
                self.dummy_tail.prev = prev_node
            # also remove the key for the cache
                key_to_remove = list(lru_node.val.keys())[0]
                del self.cache[key_to_remove]
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)