# Remove Nth Node from Linked List 
# Interesting: One Pass Approach using Fast and Slow Pointers
# Time Complexity: O(N) and Space Complexity: O(1)
# Leetcode Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ONE PASS ALGORITHM 
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sent = ListNode(-1)
        sent.next = head
        fast,slow = sent, sent
        # Make first pointer advance n+1 steps so 
        # while it reaches End, the slow pointer remains at the node before the one to be deleted
        for i in range(0, n+1):
            fast = fast.next
        # if here, the lead has been created: fast is n+1 nodes ahead of slow
        while fast is not None:
            # advance fast and slow one node at a time
            fast = fast.next
            slow = slow.next
        # if here: fast has reached the end and slow has reached node just before the desired node to be deleted
        slow.next = slow.next.next
        return sent.next 
        
        ''''
        # Approach - 1
        if head is None:
            return head
        current = head
        len_list = 0
        while current is not None:
            len_list += 1
            current = current.next
        node_num = (len_list-n)+1
        # print(node_num)
        sent = ListNode(-1)
        sent.next = head
        prev = sent
        current = head
        counter = 0
        while current and counter+1 != node_num:
            tmp = current
            counter += 1
            current = current.next 
            prev = tmp
            
        # if here counter == node_num
        print(current.val)
        print(counter)
        tmp1 = current.next
        current.next = None
        prev.next = tmp1
        return sent.next
        '''
