# Smallest Range Level 2 Problem
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/smallest-range-ii/
# Time Complexity: O(NlogN) and Space Complexity: O(N) for Sorting

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        min_A = A[0]
        max_A = A[-1]
        ans = max_A - min_A
        for i in range(0, len(A)-1):
            ans = min(ans, max(max_A-K, A[i]+K)- min(min_A+K, A[i+1]-K))
        return ans 
