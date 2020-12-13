# Remove Duplicates from Sorted Array Level-2
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# In-memory manipulation O(1) Space Complexity

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        for val in nums:
            if counter <= 1 or nums[counter-2]!=val:
                # safe to manipulate 
                nums[counter] = val
                counter += 1
        return counter 
