# Author: Pavan Kumar Paluri
# Combination Sum -II
'''
Problem Description:
-------------------
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output_list = []
        inter_list = []
        candidates = sorted(candidates)
        print(candidates)
        def helper(arr, target, inter_list, ind):
            if target ==0:
                output_list.append(inter_list)
                #print(output_list)
                #inter_list = []
            if target < 0:
                return 
            # If we exhaust the arr
            if len(arr) ==0:
                return
            '''
            for i in range(len(arr)):
                helper(arr[i:], target-arr[i], inter_list+[arr[i]])
            '''
            for i in range(ind,len(arr)):
                # since arr is sorted 
                # ignore duplicates
                if arr[i] > target:
                    continue
                
                if i > ind and arr[i]==arr[i-1]:
                    continue
                
                helper(arr, target-arr[i], inter_list+[arr[i]], i+1)
        ind = 0
        helper(candidates, target, inter_list, ind)
        return output_list
