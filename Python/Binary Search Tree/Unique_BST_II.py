# Leetcode Question: https://leetcode.com/problems/unique-binary-search-trees-ii/
# Unique Binary Search Tree: Given a value n, generate all possible BSTs
# Author: Pavan Kumar Paluri

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        else:
            def generate_trees(start, end):
                if start > end:
                    return [None, ]
                all_trees= []
                # create a root and partition into left and right subtrees
                for i in range(start, end+1):
                    # left subtree
                    left_trees = generate_trees(start, i-1)
                    # right subtree
                    right_trees = generate_trees(i+1, end)
                    
                    # explore thru the left and right within
                    for l in left_trees:
                        for r in right_trees:
                            current_tree = TreeNode(i)
                            current_tree.left = l
                            current_tree.right = r
                            all_trees.append(current_tree)
                return all_trees
            return generate_trees(1, n)
