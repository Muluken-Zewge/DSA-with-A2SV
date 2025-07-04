# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.marked = {}
        output = []
        self.findTarget(root, target.val, k)

        def dfs(node, current):
            if node is None:
                return
            if node in self.marked:
                current = self.marked[node]

            if current == 0:
                output.append(node.val)
            dfs(node.left, current - 1)
            dfs(node.right, current - 1)
        
        dfs(root, self.marked[root])
        return output


    def findTarget(self, root: TreeNode, targetValue: int, k: int) -> None:
        self.target = None
        def dfs(node):
            if node is None:
                return False
            if node.val == targetValue:
                self.target = node
                self.marked[node] = k
                return True
            if dfs(node.left) or dfs(node.right):
                existingDistPointer = node.left if node.left in self.marked else node.right
                self.marked[node] = self.marked[existingDistPointer] - 1
                return True
            return False
        dfs(root)