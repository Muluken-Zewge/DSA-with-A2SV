# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root, currentSum):
            if root is None:
                return False
            
            currentSum += root.val

            if root.left is None and root.right is None:
                return currentSum == targetSum

            return pathSum(root.left, currentSum) or pathSum(root.right, currentSum)
        
        return pathSum(root,0)
        