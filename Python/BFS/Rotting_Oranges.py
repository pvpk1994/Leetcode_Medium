# Time taken to rot oranges in a basket 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N^2)

# Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = set()
        for i in range(len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==2:
                    rotten.add((i,j))
                elif grid[i][j]==1:
                    fresh.add((i,j))
        # if here: we should have set of fresh and rotten oranges 
        #decay=set()
        timer =0
        # while there are still fresh oranges left in the basket
        while len(fresh) > 0:
            decay = set()
            for (x, y) in rotten:
                if (x+1,y) in fresh:
                    decay.add((x+1, y))
                    fresh.remove((x+1, y))
                if (x-1, y) in fresh:
                    decay.add((x-1, y))
                    fresh.remove((x-1, y))
                if (x, y+1) in fresh:
                    decay.add((x, y+1))
                    fresh.remove((x, y+1))
                if (x, y-1) in fresh:
                    decay.add((x, y-1))
                    fresh.remove((x, y-1))
            # No fresh oranges started rotting 
            if len(decay)==0:
                return -1
            timer += 1
            rotten = decay
        return timer
