# Find the nearest right node in a binary search tree
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
# Time Complexity: O(N) and Space Complexity:O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate the queue size. 
# This level could contain up to N/2 tree nodes in the case of complete BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if root is None:
            return None
        current_level, next_level = None, deque([root,])
        while next_level:
            current_level = next_level
            next_level = deque([])
            while current_level:
                current = current_level.popleft()
                if current == u:
                    return current_level[0] if len(current_level)!=0 else None
                if current.left is not None:
                    next_level.append(current.left)
                if current.right is not None:
                    next_level.append(current.right)
