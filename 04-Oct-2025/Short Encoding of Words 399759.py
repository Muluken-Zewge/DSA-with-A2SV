# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        nodes = {}
        
        for word in set(words):  # remove duplicates
            node = root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            nodes[word] = node
        
        # only count words whose node is a leaf
        return sum(len(w) + 1 for w, node in nodes.items() if not node.children)
