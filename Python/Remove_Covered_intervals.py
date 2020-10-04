# Remove Covered Intervals
# Sorting: O(NlogN) Time complexity 
# Author: Pavan Kumar Paluri

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort by ascending x-axis and if tie, by descending y-axis values 
        intervals = sorted(intervals, key=lambda x:[x[0], -x[1]])
        # print(intervals)
        result =0
        y_val = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= y_val and intervals[i][0] <= y_val:
                result += 1
            else:
                y_val = intervals[i][1]
                # print(y_val)
        # print(result)
        return len(intervals)-result 
        
