# Determine whether there exists a cycle in a given Linked List 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/linked-list-cycle/
# Challenge: Solve it using O(1) Constant space 
# Time Complexity: O(N) using 2 pointer approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return head 
        sp, fp = head, head.next
        while fp is not None:
            # At some point both slow and fast pointers converge 
            if sp==fp:
                return True
            fp = fp.next
            if fp is not None:
                sp = sp.next
                fp = fp.next
        if fp is None:
            return False 
