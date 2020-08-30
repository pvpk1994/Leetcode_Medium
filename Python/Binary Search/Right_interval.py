# Find the minimum right interval 
# Using Sorting + Binary Search in O(NlogN) time complexity
# Author: Pavan Kumar Paluri
# Problem: https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # append index to the list 
        for (x,y) in enumerate(intervals):
            intervals[x].append(x)
        print(intervals)
        # sort the intervals based on x-value, if tie: based on second value
        output = [-1]*len(intervals)
        intervals = sorted(intervals, key=lambda a:a[0])
        hi = len(intervals)-1
        low =0
        def binary_search(intervals, low, hi, target):
            while low <= hi:
                mid = low + (hi-low)//2
                if intervals[mid][0] < target:
                    low = mid+1
                else:
                    # intended target val is > mid
                    hi= mid-1
            return low if low < len(intervals) else -1
        for i in range(len(intervals)):
            val = binary_search(intervals, low, hi, intervals[i][1])
            if val != -1:
                output[intervals[i][2]] = intervals[val][2]
        return output
            
