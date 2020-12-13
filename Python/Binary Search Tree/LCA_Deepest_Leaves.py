# Find the Lowest common Ancestor for Deepest Leaves in a Binary Search Tree
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        que = deque([root,])
        level = 0
        node_vals = []
        current_1 = root 
        while que:
            n = len(que)
            node_vals.append([])
            for i in range(0, n):
                current = que.popleft()
                node_vals[level].append(current)
                if current.left is not None:
                    que.append(current.left)
                if current.right is not None:
                    que.append(current.right)
            level += 1
        # print(node_vals)
        def lca(current1, p1, p2):
            if current1 is None:
                return current1 
            if current1.val == p1 or current1.val == p2:
                return current1
            l1 = lca(current1.left, p1, p2)
            l2 = lca(current1.right, p1, p2)
            
            if l1 is not None and l2 is not None:
                return current1
            if l1 is None and l2 is None:
                return None 
            if l1 is not None:
                return l1
            else:
                return l2
        return lca(current_1, node_vals[-1][0].val, node_vals[-1][-1].val)
        # if len(node_vals[-1]) > 1:
        #     p1 = node_vals[-1][0].val
        #     p2 = node_vals[-1][1].val
        #     return lca(current_1, p1, p2)
        # else:
        #     return node_vals[-1][0]
