# Sort Linked list using O(NlogN) Merge Sort approach 
# Using Fast and Slow pointer technique 
# Author: Pavan Kumar Paluri

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def half_split(self, head:ListNode):
        current = head
        slow = head
        fast = head.next
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next 
                fast = fast.next 
        # now slow points to the exact midpoint node 
        a = head 
        b = slow.next 
        slow.next = None 
        return (a,b)
    
    def merge(self, a:ListNode, b:ListNode)->ListNode:
        # base conditions
        if a is None:
            return b
        if b is None:
            return a
        
        if a.val <= b.val:
            temp = a
            temp.next = self.merge(a.next, b)
        else:
            temp = b
            temp.next = self.merge(a, b.next)
        return temp
    
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        if head.next is None:
            return head
        
        # half-split
        a,b=self.half_split(head)
        # Now a should have the access to first node and b should have access to the mid+1 node
        print(a.val)
        print(b.val)
        a=self.sortList(a)
        b=self.sortList(b)
        
        header = self.merge(a, b)
        return header 
