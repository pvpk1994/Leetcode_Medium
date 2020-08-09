# Rotten Oranges using Breadth First Search 
# Author: Pavan Kumar Paluri
'''
Problem Description:
--------------------
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # record co-ordinates of fresh and rotten oranges 
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # populate fresh and rotten sets
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.add((i,j))
        print(fresh)
        print(rotten)
        # Population of fresh and rotten sets- done
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        timer = 0
        # iterate through rotten oranges 
        while len(fresh) >0: # as long as there are fresh oranges
            infected = set() # set to record infected ones on this iteration
            for (x,y) in rotten:
                for (i,j) in directions:
                    if ((x+i),(y+j)) in fresh:
                        # Infect the fresh orange 
                        infected.add((x+i, y+j))
                        fresh.remove((x+i, y+j))
            # if infected set is None, it means no fresh oranges have rottened in this iteration
            if len(infected) == 0:
                return -1
            # If here, add the list of infected to rotten
            rotten = infected
            # increment the timer
            timer += 1
        # If here, no fresh oranges left, all of them have rotten -> goal reached
        return timer 
        
