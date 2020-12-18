# 3 Sum problem
# Leetcode Question: https://leetcode.com/problems/3sum/
# Author: Pavan Kumar Paluri

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        output= []
        def three_sum(nums, i, output):
            low = i+1
            high = len(nums)-1
            while low < high:
                summ = nums[low]+nums[i]+nums[high]
                # Second conditions for edge case like: [-2,0,0,2,2]
                if summ < 0 or (low > i+1 and nums[low]==nums[low-1]):
                    low +=1
                elif summ >0 or (high < len(nums)-1 and nums[high]==nums[high+1]):
                    high-=1
                else:
                    output.append([nums[low], nums[i], nums[high]])
                    low += 1
                    high -=1
                    
        for i in range(0, len(nums)):
            if i ==0 or nums[i]!=nums[i-1]:
                three_sum(nums, i, output)
        return output
