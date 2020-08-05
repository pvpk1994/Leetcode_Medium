# Code Signal Problem
# Author: Pavan Kumar Paluri
'''
Problem Description:
-------------------
Example

    For

    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

    the output should be
    sudoku2(grid) = true;

    For

    grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
            ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
            ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
            ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
            ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
            ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

    the output should be
    sudoku2(grid) = false.

    The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.char grid

    A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.

    [output] boolean
        Return true if grid represents a valid Sudoku puzzle, otherwise return false.

'''
def sudoku2(grid):
    def row_check(grid, row):
        hash_set = set()
        for col in range(0, 9):
            # make sure if 
            if grid[row][col] in hash_set and grid[row][col]!='.':
                return False
            elif grid[row][col]!='.':
                hash_set.add(grid[row][col])
        return True
    
    def col_check(grid, col):
        hash_set = set()
        for row in range(0, 9):
            if grid[row][col] in hash_set and grid[row][col]!='.':
                return False 
            elif grid[row][col]!='.':
                hash_set.add(grid[row][col])
        return True
    def row_col_check(grid, start, end):
        j_start, j_end = 0, 3
        while j_start <=6:
            hash_set = set()
            for i in range(start, end):
                for j in range(j_start, j_end):
                    if grid[i][j] in hash_set and grid[i][j]!='.':
                        print(grid[i][j])
                        return False
                    elif grid[i][j]!='.':
                        hash_set.add(grid[i][j])
            j_start +=3
            j_end+= 3
        '''
        if j_start <=6 and j_end <=8:
                j_start += 1
                j_end += 1
        '''
        return True
         
    result1 = True
    result2 = True 
    result3 = True 
    for row in range(len(grid)):
        result1 = result1 and row_check(grid, row)
        result2= result2 and col_check(grid, row)
        if row <= 2:
            result3= result3 and row_col_check(grid, row*3, row*3+3)
    # print(result1)
    return result1 and result2 and result3
  
