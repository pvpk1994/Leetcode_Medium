# River Sizes
# Algo Expert 
# Author: Pavan Kumar Paluri
# Graph based problems 
# Algoexpert question: https://www.algoexpert.io/questions/River%20Sizes
# Time Complexity: O(N*M)

# solution:
def riverSizes(matrix):
    # Write your code here.
    river_sizes = []
	def dfs(row, col, curr_river_size):
		# error checks 
		if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
			return curr_river_size
		if matrix[row][col] == 0:
			# it is a land- useless
			return curr_river_size
		# if here: its river- of use
		curr_river_size +=1 
		# make the river block visited by converting it to land
		matrix[row][col] = 0
		curr_river_size = dfs(row+1, col, curr_river_size)
		curr_river_size= dfs(row-1, col, curr_river_size)
		curr_river_size= dfs(row, col+1, curr_river_size)
		curr_river_size= dfs(row, col-1, curr_river_size)
		return curr_river_size
	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[0])):
			curr_river_size = 0
			ans = dfs(row, col, curr_river_size)
			if ans > 0:
				river_sizes.append(ans)
	return river_sizes
