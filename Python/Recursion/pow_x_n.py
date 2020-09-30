# Leetcode Medium
# finding the power of (x,y)
# Author: Pavan Kumar Paluri
# Using Recursion and Fast-division Approach

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x=2 and n=3 -> 2**3 = 8
        def pow_cal(x, n):
            if n==0:
                return 1.0
            ans = pow_cal(x, n//2)
            if n%2!=0: # odd
                return ans*ans*x
            else: # even
                return ans*ans 
        if n<0:
            x=1/x
            n=-n
        return pow_cal(x, n)
