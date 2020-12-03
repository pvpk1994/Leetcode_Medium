# Increasing Binary Tree using Morris Inorder Traversal 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/increasing-order-search-tree/
# Time Complexity: O(N) and Space Complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Use morris inorder traversal 
        current = root
        tail = dummy = TreeNode()
        while current is not None:
            current1=current 
            if current.left is not None:
                new_node = current.left 
                while new_node.right is not None and new_node.right != current:
                    # proceed until the rightmost node
                    new_node = new_node.right
                # If here: we reached the last right node 
                
                    # make the current as new_nodes's right
                new_node.right = current 
                left, current.left = current.left, None
                current = left 
                
            elif current.left is None:
                # proceed to the right subtree 
                tail.right = tail = current
                current = current.right 
        return dummy.right 
