# Rotate Function 
# Author: Pavan Kumar Paluri

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        # Using DP approach 
        if len(A)==0:
            return 0
        sum_result = 0
        for i in range(0, len(A)):
            sum_result += i*A[i]
        max_elem = -math.inf
        dp = [-1 for i in range(0, len(A))]
        # print(dp)
        dp[0] = sum_result
        for i in range(1, len(A)):
            dp[i] = dp[i-1]+sum(A)-len(A)*A[len(A)-i]
        return max(dp)
        '''
        # Brute Force Approach - 14/17 
        if len(A) ==0:
            return 0
        def helper(A, max_val):
            result =0
            for i in range(0, len(A)):
                result += i*A[i]
            max_val = max(max_val, result)
            return max_val
        max_val = -math.inf
        new_A = [None for _ in range(0, len(A))]
        for k in range(0, len(A)):
            for i in range(0, len(A)):
                new_A[i] = A[(i+k)%len(A)]
            max_val = helper(new_A, max_val)
        return max_val
        '''
