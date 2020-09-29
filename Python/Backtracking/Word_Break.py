# Using Word Break 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N^2)

class Solution:
    def word_break(self, string, hash_set, start, bool_arr):
        # Using Memoization - DP 
        # O(N^2) algorithm
        # stopping condition
        if start == len(string):
            return True
        if bool_arr[start]!= None:
            return bool_arr[start]
            
        for i in range(start+1, len(string)+1, 1):
            # print(start)
            if string[start:i] in hash_set and self.word_break(string, hash_set,i, bool_arr):
                bool_arr[start]=True
                return bool_arr[start]
        bool_arr[start] = False
        return bool_arr[start]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [None]*len(s)
        return self.word_break(s, set(wordDict), 0, arr)
