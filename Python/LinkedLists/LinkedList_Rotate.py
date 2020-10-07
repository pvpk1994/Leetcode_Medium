# Rotate LinkedLists
# Author: Pavan Kumar Paluri
# Time Complexity: O(N) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if head is None:
            return None 
        if head.next is None:
            return head 
        
        # close the linked list - into a ring
        old_tail = head
        len_counter =1
        while old_tail.next is not None:
            old_tail = old_tail.next
            len_counter += 1
        # if here: we are the last node
        old_tail.next = head 
        new_tail = head
        for _ in range(0, len_counter-k % len_counter-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head 
