# Trim a Binary Search Tree
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/trim-a-binary-search-tree/
# TC: O(N) and SC:O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def bst_trim(current):
            if current is None:
                return current
            elif current.val < low:
                # root node's value is less than low 
                # Hence can eliminate all of the left subtree since all those vals < low
                return bst_trim(current.right)
            elif current.val > high:
                # root node's value is greater than high,
                # hence can eliminate all of the right subtree since all those vals > high
                return bst_trim(current.left)
            else: # values of all these nodes in the BST range(low, high)
                current.left = bst_trim(current.left)
                current.right = bst_trim(current.right)
            return current
        return bst_trim(root)
