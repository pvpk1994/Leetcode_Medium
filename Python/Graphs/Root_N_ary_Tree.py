# Find the root of a given N-ary tree whose nodes are presented in random order
# Each node has reference to its child nodes but not to its parent node
# Challenge: To solve it in constant space -O(1) and linear time O(N)
# Author: Pavan Kumar Paluri
# Leetcode question: https://leetcode.com/problems/find-root-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

#O(1) space and O(N) time
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        val_sum = 0
        for node in tree:
            val_sum += node.val
            for child in node.children:
                val_sum -= child.val
        for node in tree:
            if node.val == val_sum:
                return node 
