# Sort Linked List in an ascending order containing only 0,1,2 values
# Author: Pavan Kumar Paluri

# Trick is to gather all the counts of 0's 1's and 2's in first iteration that takes O(n)
# In second iteration, update the values of linked list with # of 0s followed by # of 1s and then #of 2s in another O(n)
# Total Time Complexity: O(n)+O(n) = O(n)

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def sortZeroOneTwoList(l):
    # traverse the list to gather n0,n1 and n2 counters
    n_0 = 0
    n_1 = 0
    n_2 = 0
    if l is None:
        return 
    root = l
    while l is not None:
        if l.value == 0:
            n_0 += 1
        elif l.value == 1: 
            n_1 += 1
        else:
            n_2 += 1
        l = l.next
    print((n_0,n_1,n_2))
    # Traversal of linkedlist done once
    # time to populate the list once again with updated values
    current = root
    while root is not None:
        while n_0 !=0:
            root.value = 0
            root = root.next
            n_0-=1
        while n_1 !=0:
            root.value = 1
            root = root.next
            n_1-=1
        while n_2 !=0:
            root.value = 2
            root = root.next
            n_2-=1
    return current 
