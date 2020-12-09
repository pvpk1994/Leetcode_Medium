# Count pair of songs whose collective runtime is divisble by 60
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        list_rem = [0 for _ in range(0, 60)]
        count = 0
        for t in time:
            # To be divisible by 60 follwoing two conditions need to be satisfied
            # 1. second % 60 ==0 if and only if first % 60 ==0 
            # 2. second % 60 = 60 - (first % 60) 
            if t % 60 == 0:
                count += list_rem[t%60]
            else:
                count += list_rem[60 - t%60]
            list_rem[t%60] += 1
        return count 
