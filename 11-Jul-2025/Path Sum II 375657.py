# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def backtrack(root, path):
            if root is None:
                return 
            path.append(root.val)

            if root.left is None and root.right is None:
                if sum(path) == targetSum:
                    ans.append(path[:])

            backtrack(root.left, path)
            backtrack(root.right, path)
            path.pop()

        backtrack(root,[])
        
        return ans
        