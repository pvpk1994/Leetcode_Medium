# Output the number of different pairs in an Array 
# Author: Pavan Kumar Paluri
# Time Complexity: O(NlogN)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        low = 0
        high =1
        result = 0
        nums = sorted(nums)
        while low < len(nums) and high < len(nums):
            if nums[high]-nums[low]<k or low==high:
                high+=1
            elif nums[high]-nums[low]>k:
                low+=1
            else:
                result+=1
                low+=1
                while low < len(nums) and nums[low]==nums[low-1]:
                    low+=1
        return result
