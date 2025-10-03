# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words):
        root = TrieNode()
        
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True
        
        best = ""
        
        def dfs(node, path):
            nonlocal best
            # update answer
            if len(path) > len(best) or (len(path) == len(best) and path < best):
                best = path
            
            for ch in sorted(node.children.keys()):  # lex order
                child = node.children[ch]
                if child.end:  # only continue if prefix is valid
                    dfs(child, path + ch)
        
        dfs(root, "")

        return best