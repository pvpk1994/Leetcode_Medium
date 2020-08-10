# LeetCode: Medium 
# Facebook Interview Question
# Author: Pavan Kumar Paluri
'''
Problem Description:
--------------------
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [-1 for i in range(len(nums))]
        R = [-1 for i in range(len(nums))]
        
        L[0] = 1 
        R[len(nums)-1] = 1
        #  populate the L and R arrays as we iterate over the list of nums
        for i in range(1, len(nums)):
            L[i] = L[i-1]*nums[i-1]
            #R[i] = R[i+1]*nums[i+1]
        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1]*nums[i+1]
        
        # Second pass to replace the values 
        for i in range(len(nums)):
            nums[i] = L[i]*R[i]
            
        return nums
 
