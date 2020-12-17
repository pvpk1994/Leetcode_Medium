# Validate Binary Search Tree 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/validate-binary-search-tree/
# Time and Space Complexities: O(N) and O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        ------- INORDER APPROACH -------
        ------- TIME COMPLEXITY: O(N) and SPACE: O(2*N) for recursion stack and node stack -------------
        prev= root.val
        list_nodes = []
        def inorder(root):
            if root is None:
                return root
            else:
                inorder(root.left)
                list_nodes.append(root.val)
                inorder(root.right)
        inorder(root)
        # print(list_nodes)
        for i in range(1, len(list_nodes)):
            if list_nodes[i] <= list_nodes[i-1]:
                return False
        return True
        #return param
        '''
        # Approach - Bound. Use hi and low to ensure the vailidity of BST
        low = -math.inf
        hi = math.inf
        def valid_bst(root, low, hi):
            if root is None:
                return True
            # edge cases: 
            if root.val <= low or root.val >= hi:
                # invalid 
                return False
            return valid_bst(root.left, low, root.val) and valid_bst(root.right, root.val, hi)
        return valid_bst(root, low, hi)
