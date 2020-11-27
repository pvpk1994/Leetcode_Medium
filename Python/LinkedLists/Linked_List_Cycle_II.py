# Advanced version of Linked List with cycles 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/linked-list-cycle-ii/
# Memory Inefficient Verison: O(N) space complexity, O(N) time complexity 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # using non-O(1) memory space 
        fp,sp = head.next, head
        hash_set = set()
        hash_set.add(sp)
        # hash_set.add(fp)
        while fp is not None:
            if fp not in hash_set:
                hash_set.add(fp)
            else:
                return fp
                
            fp = fp.next
            if fp not in hash_set:
                hash_set.add(fp)
            else:
                return fp
            if fp is not None:
                sp = sp.next
                fp = fp.next 
        if fp is None:
            return None 
