# COUNT TRIPLETS
# Author: Pavan Kumar Paluri
# Time Complexity: O(N) - single pass 
# HackerRank Question: https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps&isFullScreen=true

#!/bin/python3
from collections import defaultdict, Counter
import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
'''
# Brute Force Approach - O(N*3)
def countTriplets(arr, r):
    if len(arr) < 3:
        # no triplets can exist
        return 0
    triplet_count = 0
    for k in range(2, len(arr)):
        for j in range(1, k):
            for i in range(0, j):
                if arr[k]/arr[j] == r and arr[j]/arr[i] == r:
                    triplet_count += 1
    return triplet_count
'''
'''
def countTriplets(arr, r):
    if len(arr) < 3:
        # no triplets exist
        return 0
    hash_map = defaultdict(int)
    dict_c = Counter(arr)
    for elem in list(set(arr)):
        next_val = elem*r
        next_to_next_val = next_val*r
        if next_val in arr and next_to_next_val in arr:
            hash_map[elem] += max(dict_c[elem], dict_c[next_val], dict_c[next_to_next_val])
        else:
            hash_map[elem] = 0
    print(hash_map)
    return sum(hash_map.values())                    
'''
def countTriplets(arr, r):
    if len(arr) <= 2:
        return 0
    map_arr = {}
    map_doubles = {}
    count = 0
    # Traversing the array from rear, helps avoid division
    for x in arr[::-1]:

        r_x = r*x
        r_r_x = r*r_x

        # case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # case: x is the second element (x/r, x, x*r)
        map_doubles[(x,r_x)] = map_doubles.get((x,r_x), 0) + map_arr.get(r_x, 0)

        # case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
