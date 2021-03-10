# Smallest Difference between two given arrays
# BruteForce Approach - O(N*2) TC
# Sort: O(min(NlogN, MlogM))TC and O(1) space 
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Smallest%20Difference

### Brute Force Approach ###
import math
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # brute force solution - O(N*2)
	min_num = math.inf
	first_num, second_num = (0, 0)
	for i in range(0, len(arrayOne)):
		for j in range(0, len(arrayTwo)):
			if abs(arrayOne[i] - arrayTwo[j]) < min_num:
				min_num = abs(arrayOne[i] - arrayTwo[j])
				first_num, second_num = (arrayOne[i], arrayTwo[j])
	return [first_num, second_num]

### Optimized Approach using two pointer technique ###
import math
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # brute force solution - O(N*2)
	min_num = math.inf
	first_num, second_num = (0, 0)
	for i in range(0, len(arrayOne)):
		for j in range(0, len(arrayTwo)):
			if abs(arrayOne[i] - arrayTwo[j]) < min_num:
				min_num = abs(arrayOne[i] - arrayTwo[j])
				first_num, second_num = (arrayOne[i], arrayTwo[j])
	return [first_num, second_num]

