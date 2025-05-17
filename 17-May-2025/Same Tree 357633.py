# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, they match
        if not p and not q:
            return True
        # If one is None but the other isn't, or values differ, not the same
        if not p or not q or p.val != q.val:
            return False
        # Recurse on left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)