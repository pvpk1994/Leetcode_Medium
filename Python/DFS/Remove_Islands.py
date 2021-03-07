# Remove Islands using Iterative approach DFS
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Remove%20Islands

# Time complexity: O(R*C) Space Complexity: O(R*C) -> for auxillary matrix
def get_neighbors(matrix, row, col):
	neighbors = []
	num_rows = len(matrix)
	num_cols = len(matrix[0])
	
	if row-1>=0: # go up
		neighbors.append((row-1, col))
	if row+1 < num_rows: # go down
		neighbors.append((row+1, col))
	if col-1 >= 0: # go left
		neighbors.append((row, col-1))
	if col+1 < num_cols:
		neighbors.append((row, col+1))
	return neighbors

def connect_to_border(matrix, i, j, aux_matrix):
	stack = [(i, j)]
	while len(stack) > 0:
		curr_row, curr_col = stack.pop()
		have_visited = aux_matrix[curr_row][curr_col]
		if have_visited: # if already visited 
			continue
		# if not: mark it in the aux_matrix as visited
		aux_matrix[curr_row][curr_col] = True
		neighbors = get_neighbors(matrix, curr_row, curr_col)
		for neighbor in neighbors:
			row, col = neighbor
			if matrix[row][col] != 1:
				continue
			stack.append((row, col))

	
def removeIslands(matrix):
    # Write your code here.
	# auxillary 2D structure
	aux_matrix = [[False for col in matrix[0]]for row in matrix]
	# traversal thru the matrix
	# find all 1s that are not islands
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			i_border = i == 0 or i == len(matrix)-1
			j_border = j == 0 or j == len(matrix[0])-1
			ij_border = i_border or j_border
			if not ij_border:
				continue
			if matrix[i][j] != 1:
				continue
			connect_to_border(matrix, i, j, aux_matrix)
	# proceed with inner matrix
	for i in range(0, len(matrix)-1):
		for j in range(0, len(matrix[0])-1):
			if aux_matrix[i][j]:
				# true as in connected with the border land
				continue
			# else:
			matrix[i][j] = 0
	return matrix
    # return []
