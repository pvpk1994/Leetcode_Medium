# Find the corresponding node of a Binary Tree in a Clone of that tree
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Time Complexity: O(M+N) {M: Number of nodes in Original Tree, N: Number of nodes in cloned tree}
# Space Complexity: O(H) {H: height of BST}

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = TreeNode()
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def preorder(ori:TreeNode, cl:TreeNode):
            if ori:
                if ori is target:
                    self.ans = cl
                preorder(ori.left, cl.left)
                preorder(ori.right, cl.right)
        preorder(original,cloned)
        return self.ans
