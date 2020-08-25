// Minimize the cost for ticket purchases
// Leetcode-Medium 
// Question: https://leetcode.com/problems/minimum-cost-for-tickets/submissions/

class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        // init a dp array with all 0s
        int dp[366]= {0};
        dp[0] = 0; // since there will be no cost for no travel
        // start loading the array
        int j=0;
        for(int i=1; i<366 && j<days.size(); i++)
        {
            // if there are no travel days in between,
            // fill the dp array with previous computed dp
            if(i<days[j])
            {
                dp[i]=dp[i-1];
                continue;
            }
            // If here: i==j: safe to proceed
            // conditions
            // for a 1 day-pass 
            int a = costs[0]+dp[i-1];
            // if day is less than 7: do not add cost
            int b = (i-7 < 0) ? costs[1] : dp[i-7]+costs[1];
            int c = (i-30 < 0) ? costs[2] : dp[i-30]+costs[2];
            
            dp[i] = min(a,min(b,c));
            j++;
        }
        //for(int i=0; i<10; i++)
            //cout << dp[i] << " ";
        return dp[days[days.size()-1]];
    }
};
