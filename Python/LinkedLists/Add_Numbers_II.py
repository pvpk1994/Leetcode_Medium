# Add two numbers of two given linked lists 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/add-two-numbers-ii/

######## Approach-1 #########
# TC: O(N1+N2) {N1: len(LinkedList1), N2: len(LinkedList2)}
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method: Input linkedlists being modified by reversing of linkedlists 
# Approach: Reverse the linked-lists and perform summation 
class Solution:
    def reverse(self, head:ListNode):
        if head is None or head.next is None:
            return head
        current = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return current 
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        reverse_l1, reverse_l2 = self.reverse(l1), self.reverse(l2)
        def add_ll(reverse_l1, reverse_l2):
            if reverse_l1 is None and reverse_l2 is None:
                return None
            if reverse_l1 is None:
                return reverse_l2
            if reverse_l2 is None:
                return reverse_l1
            summ = reverse_l1.val + reverse_l2.val
            if summ < 10:
                node = ListNode(summ)
                node.next = add_ll(reverse_l1.next, reverse_l2.next)
            else: # summ > 10
                node = ListNode(summ-10)
                node.next = add_ll(ListNode(1), add_ll(reverse_l1.next, reverse_l2.next))
            return node 
        return self.reverse(add_ll(reverse_l1, reverse_l2))
   
   
 ######## Approach-2 #########
 # Challenge: Perform summation without modifying the input linked lists L1 and L2 
 # TC: O(N1+N2) and SC: O(1)
 class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp
        
        return last
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            # get the current values 
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            
            # current sum and carry
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            # move to the next elements in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head
