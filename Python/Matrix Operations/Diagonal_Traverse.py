# Traverse along the Diagonal
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/diagonal-traverse/
# Time Complexity: O(N*M) and Space Complexity: O(min(N,M))

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        inter = []
        result = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for i in range(0, num_rows+num_cols-1):
            inter = []
            if i < num_cols:
                r =0
                c = i
            else:
                r = i-num_cols+1
                c = num_cols-1
            while r < num_rows and c >-1:
                inter.append(matrix[r][c])
                r += 1
                c -= 1
            if i%2 == 0:
                result=result+inter[::-1]
            else:
                result=result+inter
        return result 
