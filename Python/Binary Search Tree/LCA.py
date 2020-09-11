# Lowest Common Ancestor in a Binary Tree using Stacks
# Depth First Search 
# Author: Pavan Kumar Paluri
# Each Node has a unique value in the Binary tree
import copy
class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Solution:
	def __init__(self):
		self.s1 = []
		self.s2 = []
		self.s11 = []
		self.s22= []
	def lca(self, root:TreeNode, n1:int, n2:int)->TreeNode:

		def h1(c1):
			if c1 is None:
				return 
			self.s1.append(c1)
			if c1.value == n1:
				# Perform a deep copy here 
				self.s11 = copy.deepcopy(self.s1)
				return
			if c1.left is not None:
				h1(c1.left)
			if c1.right is not None:
				h1(c1.right)
			self.s1.pop()
		cu1 = root
		h1(cu1)

		def h2(c2):
			if c2 is None:
				return 
			self.s2.append(c2)
			if c2.value == n2:
				self.s22 = copy.deepcopy(self.s2)
				return
			if c2.left is not None:
				h2(c2.left)
			if c2.right is not None:
				h2(c2.right)
			self.s2.pop()
		cu2 = root
		h2(cu2)
		# Enumerate through the stacks s1 and s2
		result = None
		i =0
		
		while i< min(len(self.s11), len(self.s22)) and self.s11[i].value == self.s22[i].value:
			result = self.s11[i]
			# print("Node:: "+str(result))
			i+=1
		# if here: s1[i] != s2[i]
		return result

	def lca_optimize(self, root:TreeNode, n1:int, n2:int)->TreeNode:
		if root is None:
			return None 
		if root.value == n1 or root.value == n2:
			return root

		left_node = self.lca_optimize(root.left, n1, n2)
		right_node = self.lca_optimize(root.right, n1, n2)

		if left_node is not None and right_node is not None:
			return root
		if left_node is None and right_node is None:
			return None
		# If here: either of left node is not None or right node is not None 
		if left_node is not None:
			return left_node
		else:
			return right_node 



if __name__=="__main__":
	# construct a bt
	root = TreeNode(3)
	root.left = TreeNode(6)
	root.right = TreeNode(8)
	root.left.left = TreeNode(2)
	root.left.right = TreeNode(11)
	root.left.right.left = TreeNode(9)
	root.left.right.right = TreeNode(5)
	root.right.right = TreeNode(13)
	root.right.right.left = TreeNode(7)
	sol = Solution()
	result_node = sol.lca_optimize(root, 8, 7)
	print(result_node.value)
