# Find the number of pseudo-palindromic paths in a given Binary tree
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# Time Complexity: O(N) and Space Complexity: O(N) for storing all the nodes of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_psuedo_palindrome(self, list_nodes):
        h_map = Counter(list_nodes)
        count = 0
        for val in h_map.values():
            count += val%2
        if count ==0 or count == 1:
            return True
        else:
            return False
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        list_root_leaf = []
        stack =[]
        def preorder(current):
            if current is None:
                return None
            stack.append(current.val)
            if current.left is None and current.right is None:
                # leaf node
                list_root_leaf.append(stack[:])
            preorder(current.left)
            preorder(current.right)
            stack.pop()
        preorder(root)
        count = 0
        for list_nodes in list_root_leaf:
            if self.is_psuedo_palindrome(list_nodes):
                count += 1
        return count
