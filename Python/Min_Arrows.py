# Minimum Number of arrows required to burst balloons
# Author: Pavan Kumar Paluri
# Time Complexity: O(NlogN) for sorting 

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        points = sorted(points, key=lambda x: x[1])
        y_1 = points[0][1]
        output =1
        
        for x,y in points:
            if y_1 < x:
                output+=1 
                y_1 =y
        return output
