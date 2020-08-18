# Maximum Average of N-ary tree 
# Amazon - OA 2 
# Author: Pavan Kumar Paluri
import math
class TreeNode:
	def __init__(self, value):
		self.value = value
		self.children = []
		self.root_val = 0

class Solution:
	def __init__(self):
		self.final_avg = -math.inf
	# compute the maximum average among all subtrees
	def compute_max_avg(self, root):
		if root is None:
			return 
		def dfs(root):
			# If no child is present, root.val becomes the total avg
			if not root.children:
				return (root.value, 1)
			# iterate through the list of child nodes
			temp_sum = root.value
			num_nodes = 1
			for child in root.children:
				(child_val, child_num) =dfs(child)
				temp_sum += child_val
				num_nodes += child_num

				# print(child.value)
				# temp_sum += child_sum
			if temp_sum/num_nodes > self.final_avg:
				self.final_avg = temp_sum/num_nodes
				self.root_val = root.value
			# cal avgs here:

			return (temp_sum, num_nodes)
		dfs(root)
		print("final Avg: " + str(round(self.final_avg,2)))
		print("Max Avg Node: " + str(self.root_val))
		



if __name__=="__main__":
	root = TreeNode(20)
	root.children.append(TreeNode(12))
	root.children[0].children.append(TreeNode(11))
	root.children[0].children.append(TreeNode(2))
	root.children[0].children.append(TreeNode(3))
	root.children.append(TreeNode(18))
	root.children[1].children.append(TreeNode(15))
	root.children[1].children.append(TreeNode(8))
	sol = Solution()
	sol.compute_max_avg(root)
