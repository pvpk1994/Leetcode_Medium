# Reorder LinkedLists in Python
# Author: Pavan kumar Paluri
# LeetCode-Medium 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 3 stage algorithm:
        # stage -1 : Find the mid-point in the linkedlist
        # Stage-2: Reverse the second half of the linkedlist
        # Stage-3: Merge the first half and the reversed second half such that the odd elements are occupied by the first half and even elements are occupied by the second half
        
        # base condition:
        if head is None:
            return 
        # Stage-1:
        fast, slow = head, head
        while fast.next is not None:
            fast = fast.next 
            if fast.next is not None:
                slow = slow.next
                fast = fast.next
        # If here: slow exactly at mid-pt and fast is at end of list
        # Stage-2:
        current = slow.next 
        prev = None 
        slow.next = None
        while current is not None:
            tmp = current.next
            current.next = prev
            prev = current 
            current = tmp
        # Stage-3:
        head1, head2 = head, prev
        while head2 is not None:
            tmpp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmpp 
        
