# BST traversals (Recursive + Iteraative Approaches)
# Author: Pavan Kumar Paluri
# Time Complexity: O(N)for traversal and Space Complexity: O(N) for stack 
# AlgoExpert 

######### ITERATIVE APPROACH ################
# Provide iterative solutions to all the three tree traversals
def inOrderTraverse(tree, array):
    # Write your code here.
    stack = []
	root = tree
	while stack or root:
		while root:
			stack.append(root)
			root =root.left
		# if here: root is None
		root = stack.pop()
		array.append(root.value)
		root =root.right
	return array


def preOrderTraverse(tree, array):
    # Write your code here.
    root = tree
	stack = [root,]
	while stack:
		current = stack.pop()
		array.append(current.value)
		if current.right is not None:
			stack.append(current.right)
		if current.left is not None:
			stack.append(current.left)
	return array 


def postOrderTraverse(tree, array):
    # Write your code here.
    root = tree
	stack = [root,]
	while stack:
		current = stack.pop()
		array.append(current.value)
		if current.left is not None:
			stack.append(current.left)
		if current.right is not None:
			stack.append(current.right)
	return array[::-1]
  

######## RECURSIVE APPROACH ########
# Provide iterative solutions to all the three tree traversals
def inOrderTraverse(tree, array):
    # Write your code here.
    stack = []
	root = tree
	while stack or root:
		while root:
			stack.append(root)
			root =root.left
		# if here: root is None
		root = stack.pop()
		array.append(root.value)
		root =root.right
	return array


def preOrderTraverse(tree, array):
    # Write your code here.
    root = tree
	stack = [root,]
	while stack:
		current = stack.pop()
		array.append(current.value)
		if current.right is not None:
			stack.append(current.right)
		if current.left is not None:
			stack.append(current.left)
	return array 


def postOrderTraverse(tree, array):
    # Write your code here.
    root = tree
	stack = [root,]
	while stack:
		current = stack.pop()
		array.append(current.value)
		if current.left is not None:
			stack.append(current.left)
		if current.right is not None:
			stack.append(current.right)
	return array[::-1]
