# Finding the Kth largest value in a Binary Search tree
# Using Reverse-Inorder Traversal => (right, root, left)
# Time Complexity: O(H+K), H:height of BST
# Space Complexity: O(H) 
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, num_visited, last_node_visited):
		self.num_visited = num_visited
		self.last_node_visited = last_node_visited 
		
def findKthLargestValueInBst(tree, k):
    # Write your code here.
	# initial number of visited nodes is 0 and last node visited is -1
	tree_inf = TreeInfo(0, -1)
	root = tree
	reverse_inorder(root, k, tree_inf)
    return tree_inf.last_node_visited

def reverse_inorder(root, k, tree_inf):
	if root is None or tree_inf.num_visited == k:
		return
	# reverse inorder traversal
	reverse_inorder(root.right, k, tree_inf)
	# if here: the root node is considered
	if tree_inf.num_visited < k:
		# still to explore 
		tree_inf.num_visited += 1
		# update the last visited node as the latest one
		tree_inf.last_node_visited = root.value
	# traverse the left subtree
	reverse_inorder(root.left, k, tree_inf)

