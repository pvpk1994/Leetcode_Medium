# Counting the number of islands using Depth First Search and Backtracking
# Author: Pavan Kumar Paluri
# LeetCode - Medium

class Solution:
    def dfs_helper(self, grid, i, j):
        # Check for boundary conditions
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=="0":
            return 0
        # once here, we only face 1:
        # if that is visited, sink the island-> as in make it 0.
        grid[i][j]="0"
        # now explore in all four directions
        self.dfs_helper(grid, i+1, j) # south
        self.dfs_helper(grid, i-1, j) # north
        self.dfs_helper(grid, i, j+1) # left 
        self.dfs_helper(grid, i, j-1) # right
        return 1
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # check for base condition
        if grid is None or len(grid) ==0:
            # basically no islands exist
            return 0
        # now traverse through the list to add numof islands
        numIslands =0
        for i in range(0, len(grid)): # rows
            for j in range(0, len(grid[i])): # cols
                numIslands += self.dfs_helper(grid, i, j)
        
        return numIslands
