# Palindrome Partitioning 
# Author: Pavan Kumar Paluri
# Using Dynamic Programming and BackTracking 
# Leetcode Question: https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        given a string, generate all possible palindrome outputs
        '''
        result =[]
        # 2d boolean array for storing start and i's
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # dfs_bt 
        def is_palindrome(s, low, high):
            while low < high:
                if s[low]==s[high]:
                    low+=1
                    high-=1
                else:
                    return False 
            return True
        def dfs_backtracking(start,  current, s):
            
            # Stopping condition
            
            if start >= len(s):
                result.append(current[:])
                
            # backtrack
            for i in range(start, len(s)):
                
                # If it is a palindrome --> condition still needs to be added
                if s[start]==s[i] and (i-start<=2 or dp[start+1][i-1]):
                #if is_palindrome(s, start, i):
                    dp[start][i] = True
                    current.append(s[start:i+1])
                    dfs_backtracking(i+1, current, s)
                    current.pop()
                    
        dfs_backtracking(0, [], s)
        return result
