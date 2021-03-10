# Min Max Stack Construction in Constant time and Space operations
# Author: Pavan Kumar Paluri
# Time And Space Complexity: O(1) and O(1)
# AlgoExpert Question: https://www.algoexpert.io/questions/Min%20Max%20Stack%20Construction

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.min_max_stack = []
	
	# O(1) - Time and Space
    def peek(self):
        # Write your code here.
        return self.stack[-1]
	
	# O(1) - Time and Space
    def pop(self):
        # Write your code here.
		self.min_max_stack.pop() # pop from the min_max stack as well
        elem = self.stack.pop()
		return elem
	
	# O(1) - Time and Space
    def push(self, number):
        # Write your code here.
        min_num, max_num = (number, number)
		if len(self.min_max_stack) > 0:
			prev_min, prev_max = self.min_max_stack[-1]
			min_num = min(min_num, prev_min)
			max_num = max(max_num, prev_max)
		self.min_max_stack.append((min_num, max_num))
		self.stack.append(number)
		
	# O(1) - Time and Space
    def getMin(self):
        # Write your code here.
        return self.min_max_stack[-1][0]
	# O(1) - Time and Space 
    def getMax(self):
        # Write your code here.
        return self.min_max_stack[-1][1]

