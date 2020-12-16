# Add 1 to a given linked list
# Using conept of sentenial nodes
# Time Complexity: O(N) and Space Complexity: O(1)

# Author: Pavan Kumar Paluri

# Leetcode Question: https://leetcode.com/problems/plus-one-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # create a sentinel node
        sentinal = ListNode(0)
        sentinal.next = head 
        not_nine = sentinal
        
        while head is not None:
            if head.val != 9:
                # if not 9: good to proceed but make not_9==head
                not_nine = head
            # If it is 9, stagnate the not_9 node and proceed with the head
            head = head.next
        
        # If here: head is null : So not_9 will begin its journey to the end,
        not_nine.val += 1
        not_nine = not_nine.next
        
        # Now comes the process of converting all 9s to 0s
        while not_nine is not None:
            not_nine.val = 0
            not_nine = not_nine.next
        
        # If here: head and NotNine now point to the Null (End of list)
        if sentinal.val == 0:
            return sentinal.next
        else:
            return sentinal
