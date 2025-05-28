# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node has two children
            temp = self.minValueNode(root.right)
            root.val = temp.val  # fix here too: use val, not key
            root.right = self.deleteNode(root.right, temp.val)

        return root

    def minValueNode(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left:
            current = current.left
        return current
