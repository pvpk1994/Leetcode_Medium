# Delete a Node from a Binary Search Tree
# Time Complexity: O(logN) and Space complexity: O(Recursion stack size)
# author: Pavan Kumar Paluri

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # base case 
        if root is None:
            return None 
        def successor(current: TreeNode):
            # successor: one right go until last left 
            current = current.right 
            while current.left is not None:
                current = current.left 
            return current.val
        def predecessor(current: TreeNode):
            # predecessor: One left and go until last right node
            current = current.left 
            while current.right is not None:
                current = current.right
            return current.val
        
        # if given key is > root.val -> proceed right 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # explore left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            # if here: Node itself is the key - to be deleted
            # case-1 : if node is a leaf node 
            if root.left is None and root.right is None:
                # delete the node
                root = None
            # case-2: If right node is not None
            elif root.right is not None:
                root.val = successor(root)
                # delete all the nodes 
                root.right = self.deleteNode(root.right, root.val)
            elif root.right is None:
                root.val = predecessor(root)
                # delete all the nodes 
                root.left = self.deleteNode(root.left, root.val)
        return root
