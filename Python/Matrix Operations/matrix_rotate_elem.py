# Rotate each element of given square matrix in a clockwise direction
# Author: Pavan Kumar Paluri

def matrix_rotate(arr:list)->list:
	n = len(arr)
	# Row boundaries
	top = 0
	bottom = len(arr)-1

	# Column boundaries 
	left = 0
	right = len(arr[0])-1

	while top < bottom and left < right:
		prev = arr[top+1][left]

		# Move element wise from left->right
		for i in range(left, right+1):
			current = arr[top][i]
			arr[top][i] = prev
			prev = current 
		top += 1

		# Move element wise from top->bottom
		for j in range(top, bottom+1):
			current = arr[j][right]
			arr[j][right] = prev
			prev = current 
		right -= 1

		# Move element wise from right->left 
		for k in range(right, left-1, -1):
			current = arr[bottom][k]
			arr[bottom][k] = prev
			prev = current
		bottom -=1

		# Move element wise from bottom->top
		for l in range(bottom, top-1, -1):
			current = arr[l][left]
			arr[l][left] = prev
			prev = current 
		left += 1
	return arr

if __name__ == '__main__':
	result = matrix_rotate([[1,2,3], [4,5,6], [7,8,9]])
	for elem in result:
		print(elem)