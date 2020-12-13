# Decode Ways using Memoization - DP (Top Down Approach)
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/decode-ways/

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def __init__(self):
        # Dict for memoization 
        self.memo ={}
    def recursion_ans(self, s:str, index:int):
        # if a slack '0' present:
        
        # Stopping conditions
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        
        if index == len(s)-1:
            return 1
        
        # Memoization
        if index in self.memo:
            return self.memo[index]
        
        ans = self.recursion_ans(s, index+1) + (self.recursion_ans(s, index+2) if int(s[index:index+2])<=26 else 0)
        
        # update the memoized dict 
        self.memo[index] = ans
        return self.memo[index]
    
    def numDecodings(self, s: str) -> int:
        if s is None:
            return 0
        return self.recursion_ans(s, 0)
