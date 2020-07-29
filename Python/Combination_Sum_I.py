# Author: Pavan Kumar Paluri
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

 

Constraints:

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    Each element of candidate is unique.
    1 <= target <= 500

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output_list = []
        # Concept of Backtracking
        
        def helper(candidates, target, output_list, inter_list, summ):
            # stopping conditions
            if summ == target:
                output_list.append(inter_list)
            if summ>target:
                return 
            # if we run out of elements in the candidate list
            if len(candidates) == 0:
                return
            # iterate through the candidate list
            for i in range(len(candidates)):
                helper(candidates[i:], target, output_list, inter_list+[candidates[i]],summ+candidates[i])
                
        
        if len(candidates) == 0:
            return []
        level = 0
        # output_list.append([])
        helper(candidates, target, output_list, [], 0)
        return output_list
