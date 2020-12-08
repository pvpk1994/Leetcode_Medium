# Spiral Matrix - Level 2.0
# Author: Pavan Kumar Paluri
# Inplace Matrix Manipulation - Constant Space
# Time Complexity: O(N^2) - to fill up all the elements of the matrix
# Leetcode Question: https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[None for _ in range(n)] for _ in range(n)]
        c=1
        t=n
        for i in range(0, n//2, 1):
            for j in range(i, n-1-i, 1):
                arr[i][j] = c
                arr[j][n-i-1] = arr[i][j]+(t-1)
                arr[n-1-i][n-1-j] = arr[j][n-i-1]+(t-1)
                temp = arr[n-1-j][i] = arr[n-1-i][n-1-j]+(t-1)
                c+=1
            c = temp+1
            t = t-2
        if n%2 !=0: # odd
            arr[n//2][n//2] = n*n
        return arr
