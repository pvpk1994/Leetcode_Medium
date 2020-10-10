# Construct a Binary tree from Pre and Inorder Traversals
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hash_map = {}
        low = 0
        high = len(inorder)-1
        def helper(low, high):
            if low > high:
                return None
            
            node_val = preorder.pop(0)
            root = TreeNode(node_val)
            val = hash_map[node_val]
            
            root.left = helper(low, val-1)
            root.right = helper(val+1, high)
            return root
