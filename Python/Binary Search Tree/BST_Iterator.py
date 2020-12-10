# BST iterator
# Author: Pavan Kumar Paluri
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node = root

    def next(self) -> int:
        # use morris inorder traversal
        # flatten out the BST using inorder traversal
        current = self.node
        while current is not None:
            if current.left is None:
                break
            else:
                next_node = current.left 
                while next_node.right is not None:
                    next_node = next_node.right
                # if here: reached the rightmost node 
                next_node.right = current
                left, current.left = current.left, None
                current = left 
        value = current.val
        current = current.right
        self.node = current
        return value
        

    def hasNext(self) -> bool:
        return self.node 
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
