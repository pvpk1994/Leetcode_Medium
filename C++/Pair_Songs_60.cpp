// Find the number of pairs of songs divisible by 60 
// Author: Pavan Kumar Paluri
// Time Complexity: O(N) and Space Complexity: O(N)
// Leetcode Question: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        long *rem_list;
        rem_list = new long[60]();
        int count = 0;
        for(int t=0; t<time.size(); t++)
        {
            if(time[t]%60 == 0)
                count += rem_list[0];
            else {
                // a%60 + b%60 = 60
                count += rem_list[60 - time[t]%60];
            }
            rem_list[time[t]%60]++;
        }
            return count;    
    }
};
