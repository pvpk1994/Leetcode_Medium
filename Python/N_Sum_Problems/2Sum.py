# 2 Sum problem
# Author: Pavan Kumar Paluri
# TC: O(N) and Space Complexity: O(N)
# Leetcode Question: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        uniq = set()
        for i in range(0, len(nums)):
            if target-nums[i] in uniq:
                return [i, nums.index(target-nums[i])]
            else:
                # not in uniq:
                uniq.add(nums[i])
