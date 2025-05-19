# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative approach
        ans = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                ans.append(node.val)
#since stacks are LIFO, we push right first and then left so that the next time we pop we access the left
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return ans


        #recursive approach
        # ans = []
        # def preOrder(root):
        #     if root is None:
        #         return 
        #     ans.append(root.val) 
        #     preOrder(root.left)
        #     preOrder(root.right)
        
        # preOrder(root)
        # return ans