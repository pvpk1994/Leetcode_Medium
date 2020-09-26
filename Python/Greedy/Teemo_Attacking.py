# Greedy Approach
# Teemo Attacking
# Author: Pavan Kumar Paluri
# Time Complexity: O(N)

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0:
            return 0
        total =0
        
        for i in range(0, len(timeSeries)-1):
            total += min(timeSeries[i+1]-timeSeries[i], duration)
        return total+duration
        
