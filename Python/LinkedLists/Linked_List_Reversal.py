# Reversal of a Linked List
# Author: Pavan Kumar Paluri

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def reverse_iterative(self, head:Node)->Node:
		prev = None
		current = head
		while current is not None:
			temp = current.next
			current.next = prev 
			prev = current 
			current = temp
		return prev

	def reverse_recursive(self, head:Node)->Node:
		if head is None or head.next is None:
			return head
		# by the time control reaches here, head points to the last node 
		current = self.reverse_recursive(head.next)
		# Link the head to itself
		head.next.next = head
		head.next = None
		return current 

	def print_list(self, node:Node):
		current = node
		while current is not None:
			print(current.val, end="-> ")
			current = current.next
		print("None")
		return 

if __name__ == '__main__':
	# 1->2->3->None
	root = Node(1)
	root.next = Node(2)
	root.next.next = Node(3)

	ll = LinkedList()
	# Iterative approach
	head = ll.reverse_iterative(root)
	ll.print_list(head)

	# recursive approach 
	head_1 = ll.reverse_recursive(root)
	ll.print_list(head_1)






