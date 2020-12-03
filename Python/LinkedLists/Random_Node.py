# Given a Single Linked List, Return a random node with the equal probability of picking each node 
# Author: Pavan Kumar Paluri
# Question: https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Reservoir Sampling method: 1/n 
# Time and Space Complexity: O(N), O(N)
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
    
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        prob = 1
        curr_val = 0
        current = self.head
        while current is not None:
            if random.random() < 1/prob:
                curr_val = current.val
            current = current.next 
            prob += 1
        return curr_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
