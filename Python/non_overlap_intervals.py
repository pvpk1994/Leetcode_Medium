# Author: Pavan Kumar Paluri
# LeetCode- Medium Question - Facebook 
# Problem Link: https://leetcode.com/problems/non-overlapping-intervals/solution/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlogn) approach 
        if len(intervals) ==0:
            return 0
        intervals = sorted(intervals)
        end = intervals[0][1]
        prev, count = 0,0
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
                count += 1
            else:
                prev =i
        return count 
