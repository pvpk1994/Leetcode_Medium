# 3 Sum closest problem
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/3sum-closest/
# Time Complexity: O(N^2) and Space: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        diff = math.inf
        for i in range(0, len(nums)):    
            low = i+1
            high = len(nums)-1
            while low < high:
                summ = nums[i]+nums[low]+nums[high]
                if abs(summ-target) < abs(diff):
                    diff = target -summ
                if summ < target:
                    low += 1
                else:
                    high -=1
            if diff==0:
                break
            
        return target - diff
