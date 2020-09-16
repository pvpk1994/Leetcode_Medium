# Inorder Successor given a root of BST 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/inorder-successor-in-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def right_successor(node):
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        if root is None:
            return None
        if p.right is not None:
            return right_successor(p)
        else:
            list_node = []
            def helper(root, p):
                # inorder traversal
                # inorder: [left, root, right]
                if root is None:
                    return None
                helper(root.left, p)
                if root.val > p.val:
                    list_node.append(root)
                    return root
                helper(root.right, p)
            helper(root, p)
            if len(list_node) >0:
                return list_node[0]
            else:
                return None
