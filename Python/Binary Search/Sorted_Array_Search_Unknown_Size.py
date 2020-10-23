# Search in a sorted array of unknown size 
# Author: Pavan Kumar Paluri
# Time Complexity: O(logN)
# Leetcode Question: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # If first element faced itself is the target
        if reader.get(0) == target:
            return 0
        # define boundaries
        left =0
        right = 1
        # Expand the right-end boundary until we have the following met
        while reader.get(right) < target:
            left = right
            right = right << 1
        # perform binary search
        while left <= right:
            mid = left + (right-left)//2
            if reader.get(mid) < target:
                # target lies to the right
                left = mid+1
            elif reader.get(mid) > target:
                # target lies to the left 
                right = mid-1
            else:
                return mid
        # If here: No target found
        return -1
