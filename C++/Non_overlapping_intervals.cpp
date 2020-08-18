// Author: Pavan Kumar Paluri
// Non Overlapping Intervals - LeetCode Medium Question 
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // sort the intervals (based on x-axis values) to ensure a base O(NlogN) time complexity
        sort(intervals.begin(), intervals.end());
        int overlap_counter  =0;
        int prev=0;
        for(int i=1; i<intervals.size(); i++)
        {
            // if previous y coord is greater than current x-coord
            if(intervals[prev][1]>intervals[i][0]){
                // update prev to current since we want min area overlap
                if(intervals[prev][1]>intervals[i][1])
                    prev = i;
                // increment the counter now
            overlap_counter++;
            }
            else
                prev = i;
            
        }
            
        return overlap_counter;
    }
};
