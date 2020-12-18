// Increasing Triplet Subsequence
// Author: Pavan Kumar Paluri
// Time Complexity: O(N) and Space Complexity: O(1)
// Leetcode Question: https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        long int first = LONG_MAX;
        long int second = LONG_MAX;
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i] < first)
                first = nums[i];
            else if(nums[i]<second && nums[i]>first)
                second = nums[i];
            else if(nums[i]>first && nums[i]>second)
                return true;
                
        }
        return false;
    }
};
