# Given an Array, develop a minimum height BST
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Min%20Height%20BST
# Time Complexity: O(N) and Space Complexity: O(N)

#### Approach-1 #####
# Time Complexity: O(N) and Space Complexity: O(N)
def min_ht(arr:list, st_index:int, end_index:int):
	# stopping condition
	if end_index < st_index:
		return None
	mid_index = st_index+(end_index-st_index)//2
	root_node = BST(arr[mid_index])
	root_node.left = min_ht(arr, st_index, mid_index-1)
	root_node.right = min_ht(arr, mid_index+1, end_index)
	return root_node
	
def minHeightBst(array):
	# Returns the root of the BST 
    return min_ht(array, 0, len(array)-1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
  
 ##### Approach-2 ########
 # Time Complexity: O(N) and Space Complexity: O(N)
def min_ht(arr, st_i, end_i, root):
	if end_i < st_i:
		return None
	mid_i = st_i + (end_i-st_i)//2
	new_root = BST(arr[mid_i])
	if root is None:
		# make the new_root the current root
		root = new_root
	else:
		# root node exists already 
		if arr[mid_i] < root.value:
			root.left = new_root
			root = root.left 
		else:
			root.right = new_root
			root = root.right 
	min_ht(arr, st_i, mid_i-1, root)
	min_ht(arr, mid_i+1, end_i, root)
	return root 

def minHeightBst(array):
    return min_ht(array, 0, len(array)-1, None)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
