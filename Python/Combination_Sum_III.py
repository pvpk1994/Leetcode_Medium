# Combination Sum - Level 3 
# Leet Code Medium 
# Question: https://leetcode.com/problems/combination-sum-iii/
# Author: Pavan Kumar Paluri

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        digits = [1,2,3,4,5,6, 7,8,9]
        def helper(current:list, summ:int, start:int):
            if summ > n or len(current)>k:
                return
            if summ == n and len(current) ==k:
                output.append(current[:])
            for i in range(start, len(digits)):
                if summ+digits[i] <=n:
                    helper(current+[digits[i]], summ+digits[i], i+1)
                else:
                    return 
        helper([], 0, 0)
        return output
