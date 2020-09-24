# Gas Station Problem 
# Leetcode question: https://leetcode.com/problems/gas-station/
# Author: Pavan Kumar Paluri

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = 0
        deficit = 0
        start = 0
        for i in range(0, len(gas)):
            surplus += gas[i]-cost[i]
            if surplus< 0 and i+1<len(gas):
                start = i+1
                deficit += surplus
                surplus  =0
        if surplus+deficit>=0:
            return start
        else:
            return -1
