# insert Node in a Binary Search Tree
# Author: Pavan Kumar Paluri
# Time Complexity: O(Height of Tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # Explore left subtree if given val < node's val
        # Explore right subtree if given val > nodes val 
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right=self.insertIntoBST(root.right, val)
        return root
