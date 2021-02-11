# Number of Distinct Islands 
# Author: Pavan Kumar Paluri
# Time Complexity: O(M*N) {M:Number of rows and N: Number of Columns}
# Space Complexity: O(M*N) 
# Leetcode Question: https://leetcode.com/problems/number-of-distinct-islands/

class Solution:    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        def is_current_island_uniq():
            #  cell by cell comparison with all the islands in uniq_islands
            
            for uniq_island in uniq_islands:
                marker = False
                if len(uniq_island) != len(current_island):
                    # no match 
                    continue
                for c1, c2 in zip(current_island, uniq_island):
                    # cell by cell comparison
                    if c1 != c2:
                        # mismatch occurred, islands are different
                        marker = True
                        break
                # if here: cell by cell match was successfull
                if not marker:
                    return False
            return True
        '''
        def dfs(row, col):
            # error checks
            if row < 0 or row >=len(grid) or col < 0 or col >= len(grid[0]):
                return
            # if water or the island is already visited ?
            if grid[row][col] ==0 or (row, col) in visited_islands:
                return
            # if here: island is visited
            visited_islands.add((row, col))
            current_island.add((row-row_origin, col-col_origin))
            # bring it to local co-ordinates
            
            # explore the neighboring cells
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            
        visited_islands = set()
        uniq_islands = set()
        # traverse the matrix of islands and water
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                # if here: 
                # shape comparison
                if current_island: # if its a valid set. 
                    # making current_island a frozen set will make it immutable. 
                    # therefore can be added to uniq_islands
                    uniq_islands.add(frozenset(current_island))
        return len(uniq_islands)
