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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next 
            n1 += 1
        while curr2:
            curr2 = curr2.next 
            n2 += 1
            
        # parse both lists
        # and sum the corresponding positions 
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val 
                curr1 = curr1.next 
                n1 -= 1
            if n1 < n2:
                val += curr2.val 
                curr2 = curr2.next
                n2 -= 1
                
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next
        
        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head
