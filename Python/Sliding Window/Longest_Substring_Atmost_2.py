# Longest Substring with atmost 2 distinct characters 
# Author: Pavan Kumar Paluri
# Using Sliding window + HashMap
# Time Complexity: O(N) and Space Complexity: O(2) - Constant Space since hashmap always holds 2 elements at max
# Leetcode Question: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # base case: if len(s) ==0
        if len(s)==0:
            return 0
        h_map={}
        left,right = 0,0
        h_max = 1
        while right < len(s):
            h_map[s[right]] = right
            right +=1
            if len(h_map)==3:
                # Just greater than 2
                del_index = min(h_map.values())
                del h_map[s[del_index]]
                left = del_index+1
            h_max = max(h_max, right-left)
        return h_max
