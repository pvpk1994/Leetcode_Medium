# Design Linked List - Single or Double
# Auhtor: Pavan Kumar Paluri
# Question: https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, x):
        self.val = x
        self.next =  None
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=0
        self.head = Node(0) # psuedo-head node
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index+1):
            current = current.next
        # if here: current 
        return current.val
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        # if index is negative, node will be inserted at the head of the list
        if index < 0:
            index  = 0
        # find the predecessor of the node to be added
        pred = self.head
        self.size+=1
        for _ in range(index): # goes until predecessor
            pred = pred.next
        # node to be added 
        to_add = Node(val)
        # insert this node
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return None
        # deletion of the node: decrement the size by 1 unit
        self.size -= 1
        # find predecessor of the node to be deleted 
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
