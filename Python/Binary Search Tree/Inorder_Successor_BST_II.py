# Leetcode Medium question: https://leetcode.com/problems/inorder-successor-in-bst-ii/
# Author: Pavan Kumar Paluri
# Inorder Successor in Binary Search Tree - Level 2 
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def right_successor(self, root):
        # proceed one step to right
        root = root.right
        while root.left is not None:
            root = root.left
        # If here root.left is None, so return root
        return root

    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        # Inorder traversal in a BST
        if node.right is None:
            # traverse back to the other
            if node.parent is not None and node.parent.val > node.val:
                return node.parent
            else: # node's parent is still < node's val
                while node.parent is not None and node.parent.val < node.val:
                    node = node.parent
                # If here: node.parent > node
                return node.parent 
            
            
        # If right node exists, determine its successor
        elif node.right is not None:
            return self.right_successor(node)
        
