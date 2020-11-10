# Rotate a given matrix by 90 degrees
# Author: Pavan Kumar Paluri

def rotate_clockwise(mat:list)->list:
	# border condition check 
	if len(mat) < 1:
		return 
	n = len(mat)
	for i in range(0, n//2):
		for j in range(i, n-1-i):
			saved = mat[i][j]
			mat[i][j] = mat[n-1-j][i]
			mat[n-1-j][i] = mat[n-1-i][n-1-j]
			mat[n-1-i][n-1-j] = mat[j][n-1-i]
			mat[j][n-1-i] = saved
	return mat

if __name__ == '__main__':
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	new_matrix=rotate_clockwise(matrix)
	# print([elem for elem in new_matrix], end="\n")
	for elem in new_matrix:
		print(elem)
		# print("\n")