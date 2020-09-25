# Largest Difference in a group of numbers
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/largest-number/
# Time complexity: O(NlogN). Space Complexity: O(N)

class Sol(str):
    def __lt__(x,y):
        return x+y >y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ln = ''.join(sorted(map(str, nums), key=Sol))
        if ln[0]=="0":
            return "0"
        else:
            return ln
