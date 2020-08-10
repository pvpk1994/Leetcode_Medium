# Author: Pavan Kumar Paluri
# Add two numbers in a given linked list 
# Hack: Need to carefully handle carry-over of 1 that can cause overflows to occur 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1 
        summ = 0
        carry = 0
        curr1 = l1
        curr2 = l2
        def helper(curr1, curr2):
            if curr1 is None:
                return curr2
            if curr2 is None:
                return curr1
            if curr1 is not None and curr2 is not None:
                summ1 = curr1.val + curr2.val 
                if summ1 < 10:
                    new_node = ListNode(summ1)
                    carr = 0
                    print(summ1)
                    new_node.next = helper(curr1.next, curr2.next)
                else:
                    summ1 = summ1-10
                    carr=1
                    new_node = ListNode(summ1)
                    print(summ1)
                    # Key here is to create a carry-over node and inclue it in the helper function 
                    new_node.next =helper(ListNode(1), helper(curr1.next, curr2.next))
            return new_node
        return helper(curr1, curr2)
