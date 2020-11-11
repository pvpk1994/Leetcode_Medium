# Anti Clockwise rotation of Matrix
# Author: Pavan Kumar Paluri

def matrix_anticlockwise(matrix:list)->list:
	n = len(matrix)
	for i in range(0, len(matrix)//2):
		for j in range(i, len(matrix)-1-i):
			saved = matrix[i][j]
			matrix[i][j] = matrix[j][n-1-i]
			matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
			matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
			matrix[n-1-j][i] = saved
	return matrix

if __name__ == '__main__':
	# given_matrix = [[1,2,3], [4,5,6], [7,8,9]]
	given_matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
	result =matrix_anticlockwise(given_matrix)
	for elem in result:
		print(elem)