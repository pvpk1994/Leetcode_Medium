# House Robber Problem
# Dynamic Programming
# Author: Pavan Kumar Paluri
# Leetcode question: https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # base condition
        if len(nums) == 0: # no house to rob
            return 0
        if len(nums) == 1: # only one house to rob
            return nums[0]
        if len(nums) == 2: # return max of houses
            return max(nums[0], nums[1])
        # construct a dp 
        dp = [0]*len(nums)
        dp[0] = nums[0]
        # robbing either 0th or 1st house
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        # return the last element 
        return dp[-1]
