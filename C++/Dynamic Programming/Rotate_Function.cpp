// Rotate Function in O(N)
// Author: Pavan Kumar Paluri
// LeetCode Question: https://leetcode.com/problems/rotate-function/

class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        if(A.size()==0)
            return 0;
        int sum_result =0;
        for(int i=0; i<A.size(); i++)
        {
            sum_result += i*A[i];
        }
        long int sum =0;
        for(int i=0; i<A.size(); i++)
            sum += A[i];
        // Assign a new vector dp of same size as A
        vector<int>dp (A.size());
        dp[0] = sum_result;
        for(int i=1; i<A.size(); i++)
        {
            dp[i] = dp[i-1] + sum - A.size()*A[A.size()-i];
        }
        return *max_element(dp.begin(), dp.end());
    }
};
