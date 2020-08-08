# Medium LeetCode Question
# Concept Walkthrough: https://www.youtube.com/watch?v=6jYxwdwjwKg
'''
Problem Description:
--------------------
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter  =0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def helper(root, prev_sum):
            if not root:
                return
            current_sum = prev_sum + root.val
            diff = current_sum - sum
            if diff in my_dict:
                self.counter += my_dict[diff]
            if current_sum in my_dict:
                my_dict[current_sum] += 1
            else:
                my_dict[current_sum] = 1
            helper(root.left, current_sum)
            helper(root.right, current_sum)
            # If here: end of branch reached, so delete the path traced i.e., current_sum
            my_dict[current_sum] -= 1
        my_dict = {0:1}        
        helper(root, 0)
        return self.counter
