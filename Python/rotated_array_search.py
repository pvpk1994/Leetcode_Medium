# Binary Search in a rotated array 
# Author: Pavan Kumar Paluri
'''
Problem Description:
--------------------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Single Pass Binary Search
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if nums[mid] > target and nums[low] <= target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target and nums[high] >= target:
                    low=mid+1
                else:
                    high=mid-1
        return -1
 
