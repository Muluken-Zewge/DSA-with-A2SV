# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #funtion to check if a node isvalid recursively
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))
