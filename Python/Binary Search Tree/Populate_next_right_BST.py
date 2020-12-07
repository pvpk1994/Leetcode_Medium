# Populate next right pointers in Binary Search Tree
# Auhtor: Pavan Kuamr Paluri
# Time Complexity: O(N) and space Complexity: O(N)
# Leetcode Question: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root 
        que =deque([root,])
        level = 0
        while que:
            len_q = len(que)
            for i in range(0, len_q):
                current = que.popleft()
                if i < len_q-1:
                    current.next = que[0]
                if current.left is not None:
                    que.append(current.left)
                if current.right is not None:
                    que.append(current.right)
            level = level+1 
        # if here: list_nodes is going to have appropriate nodes arranged
        return root
