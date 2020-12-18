# 3 Sum Smaller Problem 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N^2) and Space Complexity: O(1)
# Leetcode Question: https://leetcode.com/problems/3sum-smaller/

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)
        counter =0
        def three_small(nums, new_target, low):
            counter = 0
            lower = low
            high = len(nums)-1
            while lower < high:
                summ = nums[lower]+nums[high]
                if summ < new_target:
                    counter += high - lower
                    lower +=1
                else:
                    high -=1
            return counter
        for i in range(0, len(nums)-2):
            counter += three_small(nums, target-nums[i], i+1)
        return counter 
