# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        #use BFS(level order traversal)
        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            prev_val = None #prev_val is None for all first nodes in the level
            
            for _ in range(level_size):
                node = queue.popleft()
                val = node.val
                #for even levels
                if level % 2 == 0:
                    if (val % 2 == 0) or (prev_val is not None and val <= prev_val):
                        return False
                #for odd levels
                else:
                    if (val % 2 == 1) or (prev_val is not None and val >= prev_val):
                        return False
                #set val to prev_val for the next iteration
                prev_val = val
                #append the left and right of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            #increment the level for the next level
            level += 1
        
        return True