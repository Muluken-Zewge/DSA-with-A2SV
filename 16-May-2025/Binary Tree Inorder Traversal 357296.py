# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(node):
            if not node:
                return []
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        return ans

#iterative approach
        # ans = []
        # stack = []
        # curr = root
        # while curr or stack:
        #     #reach most left node
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     #access left most node
        #     node = stack.pop()
        #     ans.append(node.val)
        #     #move to the right node
        #     node = node.right
        #     #reset curr to find the left most left element of it
        #     curr = node

        # return ans
