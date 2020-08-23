# problem: https://leetcode.com/problems/the-maze/
# Using DFS - to explore the solution space until the destination is met where ball stops
# Author: Pavan Kumar Paluri

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        row_len = len(maze)
        col_len = len(maze[0])
        visited_nodes = set()
        start = tuple(start)
        end = tuple(destination)
        
        def move(pos):
            if pos in visited_nodes:
                return False
            # if pos is the destination:
            if pos == end:
                return True
            # if here: add it to the visited list
            visited_nodes.add(pos)
            
            # explore every direction (NEWS)
            for direction in range(4):
                x,y = pos
                if direction == 0: # Up/ North
                    # proceed until we do not hit the wall
                    while y>0 and maze[x][y-1]==0:
                        y-=1
                if direction == 1: # Down/South
                    while y<col_len-1 and maze[x][y+1]==0:
                        y+=1
                if direction == 2: # West/Left
                    while x>0 and maze[x-1][y]==0:
                        x-=1
                if direction == 3: # East/Right
                    while x<row_len-1 and maze[x+1][y]==0:
                        x+= 1
                if move((x, y)):
                    # destination reached 
                    return True
        return move(start)
