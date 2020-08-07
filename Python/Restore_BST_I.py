'''
Restore Binary Search Tree given list of inorder and preorder traversals
Author: Pavan Kumar Paluri
'''
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
    # hashmap for inorder
    hashmap_inorder = {}
    # load the hashmap
    def helper(left_index, right_index):
        if left_index > right_index:
            return None 
        if preorder:
            root_val = preorder.pop(0)
            root_node = Tree(root_val)
            
            inorder_index = hashmap_inorder[root_val]
            root_node.left = helper(left_index, inorder_index-1)
            root_node.right = helper(inorder_index+1, right_index)
            return root_node
        
    for val in enumerate(inorder):
        hashmap_inorder[val[1]] = val[0]
    return helper(0, len(inorder)-1)
     
