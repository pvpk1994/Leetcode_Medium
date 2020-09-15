# House Robber - Level 2 
# Last House is connected to the first house and therefore robbery cannot happen in last and first houses 
# Leetcode Question: https://leetcode.com/problems/house-robber-ii/
# Author: Pavan Kumar Paluri

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Key here is since last house is connected to the first house
        # if first house is robbed, then last house cannot be robbed
        # if last house is robbed, then first house cannot be robbed
        # therefore, we can split the list into parts with first list not containing last house
        # second list not containing first house
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def rob_simple(new_nums: List):
            if len(new_nums) == 0:
                return 0
            if len(new_nums) == 1:
                return new_nums[0]
            if len(new_nums) == 2:
                return max(new_nums[0], new_nums[1])
            dp = [-1]*len(new_nums)
            dp[0] = new_nums[0]
            dp[1] = max(dp[0], new_nums[1])
            for i in range(2, len(new_nums)):
                dp[i] = max(dp[i-1], dp[i-2]+new_nums[i])
            return dp[-1]
        return max(rob_simple(nums[1:]), rob_simple(nums[:len(nums)-1]))
