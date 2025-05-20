# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #itertative approach
        #modified preorder reverse(root -> right -> left) and reverse the ans
        ans = []
        if root is None:
            return ans
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return ans[::-1]

        #recursive approach
        ans = []
        def postOrder(root):
            if root:
                postOrder(root.left)
                postOrder(root.right)
                ans.append(root.val)
        
        postOrder(root)
        return ans
