# Longest Increasing Subsequence using Dynamic Programming
# Author: Pavan Kumar Paluri
# Time Complexity: O(N^2) and Space Complexity: O(N) -> for DP array 
# Leetcode Question: https://leetcode.com/problems/longest-increasing-subsequence/

# Time Complexity: O(N^2) and Space Complexity: O(N)
# Using Dynamic Programming 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        max_ans = 1
        dp = [0]*len(nums)
        dp[0]=1
        for i in range(1, len(dp)):
            max_val =0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j])
            dp[i] = max_val+1
            max_ans = max(max_ans, dp[i])
            
        return max_ans
