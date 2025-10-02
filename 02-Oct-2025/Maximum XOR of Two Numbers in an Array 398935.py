# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        # each node has at most two children: 0 or 1
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        
        def insert(num):
            node = root
            for i in range(31, -1, -1):  # 31..0, from the constraints
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        def query(num):
            node = root
            xor_sum = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit  # opposite bit
                if node.children[toggled]:
                    xor_sum |= (1 << i)  # set this bit in result
                    node = node.children[toggled]
                else:
                    node = node.children[bit]
            return xor_sum
        
        # Insert all numbers
        for num in nums:
            insert(num)
        
        # Find maximum XOR
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, query(num))
        
        return max_xor
