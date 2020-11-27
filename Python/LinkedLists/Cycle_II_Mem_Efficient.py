# Memory Efficient Linked List Cycle Detection alg
# Author: Pavan Kumar Paluri
# O(N) and O(N) Time and Space complexities
# Leetcode Question: https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def is_intersect(self, head)->ListNode:
        if head is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
            if fast == slow:
                return slow
        
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head 
        intersection = self.is_intersect(head)
        # fast and slow pointers
        first = head
        second = intersection
        # print(first.val)
        # print(second.val)
        if second is None:
            return None 
        while first!=second:
            first = first.next
            second = second.next 
        
        # If here, the entrance point to cycle is obtained,
        return first 
