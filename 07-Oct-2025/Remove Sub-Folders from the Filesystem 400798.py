# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        folder.sort()  # ensures parents come before children
        res = []

        for path in folder:
            parts = path.split("/")[1:]  # skip leading ""
            node = root
            skip = False
            for p in parts:
                if node.is_end:  # parent folder already marked
                    skip = True
                    break
                if p not in node.children:
                    node.children[p] = TrieNode()
                node = node.children[p]
            if not skip:
                node.is_end = True
                res.append(path)

        return res
