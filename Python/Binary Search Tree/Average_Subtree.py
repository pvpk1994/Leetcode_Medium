# Author: Pavan Kumar Paluri
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_avg = 0
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # If root node is None: return 0
        if root is None:
            return 0
        # node = root
        def dfs(node):
            # if node is None: return 0 for val_sum and 0 for node_count
            if node is None:
                return (0, 0)
            # explore left subtree and compute the val_sum and node_count
            val_left_sum, node_left_count = dfs(node.left)
            
            # Similarly, explore the right subtree and compute the val_sum and node_count for right subtree
            val_right_sum, node_right_count = dfs(node.right)
            
            # Calculate the total val_sum including the current node
            val_sum = val_left_sum + val_right_sum + node.val
            
            # Calculate the total node count including the current node
            node_count = node_left_count + node_right_count + 1
            
            # compute the avg
            avg_val = val_sum / node_count
            
            if avg_val >= self.max_avg:
                self.max_avg = avg_val
                
            # return the val_sum and node_count to previous stack call
            return (val_sum, node_count)
        
        dfs(root)
        return self.max_avg
