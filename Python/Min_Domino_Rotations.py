# Minimum Domino Rotations needed to attain equal Row of values
# Author: Pavan Kumar Paluri

# ----------------------
# Time Complexity: O(N)
# Space Complexity: O(N)
# -----------------------

from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        c_a = Counter(A)
        c_b = Counter(B)
        max_a = -math.inf 
        max_b = -math.inf
        for key, val in c_a.items():
            if max_a < val:
                max_a = val
                key_a = key
        for key, val in c_b.items():
            if max_b < val:
                max_b = val
                key_b = key
        if max_a < max_b:
            # majority always in B
            final_val = max_b
            final_key = key_b
            A,B=B,A
            
        else:
            final_val = max_a
            final_key = key_a
            
        num_rotations = 0
        for a,b in zip(A, B):
            if final_key == a:
                continue
            else:
                if final_key == b:
                    num_rotations += 1
                else:
                    return -1
        return num_rotations 
