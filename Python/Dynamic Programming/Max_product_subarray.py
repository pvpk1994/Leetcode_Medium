# Question: https://leetcode.com/problems/maximum-product-subarray/
import math
# Single Pass O(N)  DP Solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # construct left and right arrays that hold cumulative product until that point
        if len(nums)==0:
            return 0
        placeholder_result = nums[0]
        min_num = nums[0]
        max_num = nums[0]
        current_num = nums[0]
        
        for i in range(1, len(nums)):
            current_num = nums[i]
            old_min = min_num
            min_num = min(min_num*current_num, current_num, max_num*current_num)
            max_num = max(old_min*current_num, current_num, max_num*current_num)
            
            if placeholder_result < max(max_num, min_num, current_num):
                placeholder_result = max(max_num, min_num, current_num)
        return placeholder_result 
