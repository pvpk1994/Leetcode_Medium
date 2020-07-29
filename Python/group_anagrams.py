# Author: Pavan Kumar Paluri
# Time Complexity: O(N^2 logN)
'''
Problem Description:
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = defaultdict(list)
        for string in strs:
            dict_strs[tuple(sorted(string))].append(string)
        return list(dict_strs.values())
 
