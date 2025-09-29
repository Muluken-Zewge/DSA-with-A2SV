# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0   # sum of all words passing through this node

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}   # stores current values of keys

    def insert(self, key: str, val: int) -> None:
        # find old value (default 0 if key not seen)
        old_val = self.map.get(key, 0)
        diff = val - old_val
        self.map[key] = val

        curr = self.root
        curr.value += diff  # update root sum too
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.value += diff  # update sums down the path

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.value
