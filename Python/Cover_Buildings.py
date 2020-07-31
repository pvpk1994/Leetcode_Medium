'''
Author: Pavan Kumar Paluri
Problem Description:
There are N rectangular buildings standing along the road next to each other. The K-th building is of size H[K] × 1.

Because a renovation of all of the buildings is planned, we want to cover them with rectangular banners until the renovations are finished. Of course, to cover a building, the banner has to be at least as high as the building. We can cover more than one building with a banner if it is wider than 1.

For example, to cover buildings of heights 3, 1, 4 we could use a banner of size 4×3 (i.e. of height 4 and width 3), marked here in blue:

Buildings of sizes (3 × 1), (1 × 1), (4 × 1), covered with scaffolding of size 4×3

We can order at most two banners and we want to cover all of the buildings. Also, we want to minimize the amount of material needed to produce the banners.

What is the minimum total area of at most two banners which cover all of the buildings?

Write a function:

    def solution(H)

that, given an array H consisting of N integers, returns the minimum total area of at most two banners that we will have to order.

Examples:

1. Given H = [3, 1, 4], the function should return 10. The result can be achieved by covering the first two buildings with a banner of size 3×2 and the third building with a banner of size 4×1:

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
import math
def solution(H):
    # write your code in Python 3.6
    total_canvas_units = 2
    canvas_len = len(H)
    max_from_left = []
    max_from_right = []
    
    # Base Case: If the number of buildings is 1:
    if len(H)==1:
        return H[0]*1
    # Base-case-1: If there are no buildings, no cnavas needed;
    if H is None:
        return 0
    current_max = 0
    # Assign the left-max in the array to current_max
    for i in range(canvas_len):
        if current_max >= H[i]:
            current_max = current_max
        else:
            current_max = H[i]
        max_from_left.append(current_max)
    
    # do the same from right
    # reset current max
    current_max = 0
    for i in range(canvas_len-1, -1, -1):
        if current_max >= H[i]:
            current_max = current_max
        else:
            current_max = H[i]
        max_from_right.append(current_max)
    
    # Reverse max_from right
    max_from_right = max_from_right[::-1]
    # print(max_from_left)
    # print(max_from_right)
    result = math.inf
    for i in range(1, canvas_len):
        result = min(result, max_from_left[i-1]*(i) + max_from_right[i]*(canvas_len-i))
        
    return result
 
if __name__=="__main__":
    print(solution([1,1,7,6,6,6]))
