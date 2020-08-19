// Counting the number of islands in a given 2D matrix
// Author: Pavan Kumar Paluri
// Leetcode - Medium
// Approach used: DFS + Backtracking

class Solution {
public:
    int dfs_helper(vector<vector<char>>&grid, int row, int col)
    {
        // chack for base conditions
        if(row<0 || row>=grid.size() || col<0 || col>=grid[row].size() || grid[row][col]=='0') 
            return 0;
        // if here, valid cases only - as in islands with 1
        // if an island is visited- sink it- change it to 0
        grid[row][col]='0';
        // explore cardinal directions to see if we can get extended islands
        dfs_helper(grid, row+1, col); // down
        dfs_helper(grid, row-1, col); // up
        dfs_helper(grid, row, col+1); // right
        dfs_helper(grid, row, col-1); // left 
        return 1;
    }
    
    int numIslands(vector<vector<char>>& grid) {
        // check base conditions
        if(grid.size() == 0 || grid.empty())
            return 0;
        // if here: grid is valid one
        int num_islands  =0;
        for(int i=0; i<grid.size(); i++)
        {
            for(int j=0; j<grid[i].size(); j++)
            {
                num_islands += dfs_helper(grid, i, j);
            }
        }
        
        return num_islands;
    }
};
