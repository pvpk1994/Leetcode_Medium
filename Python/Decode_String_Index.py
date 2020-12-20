# Decode String Index based on the string decoding and Expanding
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/decoded-string-at-index/
# Time and Space Complexity: O(N) and O(1)

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # compute the size of the decoded string
        size = 0
        for s in S:
            if s.isdigit():
                size= size*int(s)
            else:
                size += 1
        
        # Now compute the right index char based on K and S
        for s in reversed(S):
            K = K%size
            if K==0 and s.isalpha():
                return s
            
            if s.isdigit():
                size = size/int(s)
            elif s.isalpha():
                size -=1
