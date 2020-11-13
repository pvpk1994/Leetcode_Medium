# Robinhood interview question 
# Author: Pavan Kumar Paluri
# Rotate Matrix clockwise and output the state of rotated box given the following conditions

'''
Conditions:
----------
1. '#' -> represents a small box
2. '.' -> Free state / empty slot
3. '*' -> Obstacle

When an obstacle is encountered, all the boxes above it can rest on this obstacle.
Else all the boxes will fall to the bottom of the matrix due to gravity.
'''

def matrix_rotate(arr:list):
	num_rows = len(arr)
	num_cols = len(arr[0])
	new_arr = [[None for _ in range(0,num_rows)] for _ in range(0,num_cols)]
	for i in range(num_rows-1, -1, -1):
		for j in range(0, num_cols, 1):
			new_arr[j][num_rows-1-i] = arr[i][j]
	return new_arr

def matrix_fall(arr:list):
    # access every column first
    for j in range(0, len(arr[0])):
        # access every row next -> from bottom to top
        for k in range(len(arr)-1, -1, -1):
            # acess every row from k until the end of the matrix
            for l in range(k, len(arr)-1, 1):
                if arr[l][j] == '#' and arr[l+1][j] == '.': # Small box followed by empty space
                    # Simply swap
                    arr[l][j], arr[l+1][j] = arr[l+1][j], arr[l][j]
                else:
                    break
    return arr

if __name__ == '__main__':
	# result = matrix_rotate([['a','b','c'], ['d','e','f']])
    '''
    result_rotate = matrix_rotate([['#', '#', '.', '.', '.', '.', '.'],
							       ['#', '#', '#', '.', '.', '.', '.'],
							       ['#', '#', '#', '.', '.', '#', '.']])
    '''
    result_rotate = matrix_rotate([['#', '#', '.', '.', '.', '#', '.'],
                                   ['#', '#', '#', '.', '.', '*', '.'],
                                   ['#', '#', '#', '*', '.', '#', '.']])
    result_fall = matrix_fall(result_rotate)
    for elem in result_fall:
        print(elem)
