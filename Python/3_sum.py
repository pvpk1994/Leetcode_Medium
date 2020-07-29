# Author: Pavan Kumar Paluri
# LeetCode - medium
'''
Description:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        if len(nums) == 0:
            return []
        if len(nums)>0 and nums[0] > 0:
            return []
        output= []
        def helper(nums, i, low, hi, output):
            low = i+1
            while low < hi:
                summ = nums[i] + nums[low] + nums[hi]
                if summ < 0 or (low>i+1 and nums[low]==nums[low-1]):
                    low +=1
                elif summ > 0 or (hi <len(nums)-1 and nums[hi]==nums[hi+1]):
                    hi -=1
                else:
                    # output+=[nums[i], nums[low], nums[hi]]
                    output.append([nums[i], nums[low], nums[hi]])
                    #output.append(nums[i])
                    low +=1
                    hi -=1
        low=0
        hi = len(nums)-1
        for i in range(0, len(nums)):
            if i==0 or (nums[i]!=nums[i-1]):
                helper(nums, i, low, hi, output)
        
        
        return output
                
 
