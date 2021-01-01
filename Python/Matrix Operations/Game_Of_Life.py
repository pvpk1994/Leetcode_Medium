# Game of life following all the given rules 
# Desired Space complexity: O(1) - In place manipulation
# Current solution has O(M*N) space complexity - Needs to be optimized.
# Time Complexity: O(M*N)
# Leetcode Question: https://leetcode.com/problems/game-of-life/

# Time Complexity: O(M*N) Space Complexity: O(M*N) for backing up a whole matrix 
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # copy matrix
        copy_matrix = [[board[row][col] for col in range(len(board[0]))] for row in range(len(board))]
        
        # 8 possible directions
        directions = [(0,1), (0, -1), (1,0), (-1,0), (-1,-1), (1,1), (1,-1), (-1,1)]
        num_rows = len(board)
        num_cols = len(board[0])
        
        # matrix traversal
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                # for each cell, explore all of its neighboring cells
                num_live_cells = 0
                for direction in directions:
                    r = i + direction[0]
                    c = j + direction[1]
                    # make sure if it is a live cell 
                    if (r < num_rows and r >=0) and (c < num_cols and c>=0) and (copy_matrix[r][c]==1):
                        # if it is live cell, increment live_cell_count
                        num_live_cells +=1
                # if here: We now have estimate of surrounding live cells
                # start applying rules 
                # Rule-1: Any live cell with fewer than 2 live neighbors die
                # Rule-2: Any live cell with 2/3 live neighbors live up
                # Rule-3: Any Live cell with > 3 live neighbors die
                # Rule-4: Any dead cell with ==3 live neighbors becomes alive
                if copy_matrix[i][j] == 1 and (num_live_cells > 3 or num_live_cells < 2):
                    # Rule-1 and Rule-3: So the current cell dies...
                    board[i][j] = 0
                if copy_matrix[i][j] == 0 and num_live_cells == 3:
                    # Rule-4: Dead becomes alive
                    board[i][j] = 1
                # Rule-2 is taken care by default.
