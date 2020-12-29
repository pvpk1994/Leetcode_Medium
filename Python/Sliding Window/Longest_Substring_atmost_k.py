# Longest Substring with atmost K distinct characters 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N) and Space Complexity: O(K) for hash-Map
# Leetcode Question: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Example : l o v e l e e t c o d e
        if len(s)==0 or k==0:
            return 0
        left,right = 0,0
        h_map= {}
        max_len = 1
        while right < len(s):
            h_map[s[right]] = right
            right += 1
            if len(h_map) == k+1: # just greater than k elements
                # delete the character with lowest index i.e., leftmost character
                id_del = min(h_map.values())
                del h_map[s[id_del]]
                # now increment the left pointer to the character that is just right to 
                # the id_del
                left = id_del +1 
            max_len = max(max_len, right-left)
        return max_len
