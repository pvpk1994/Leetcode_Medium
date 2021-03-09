# Single Cycle Check in a Uni dimensional Array
# Author: Pavan Kumar Paluri
# Time Complexity: O(N) and Space Complexity: O(1)
# AlgoExpert Question: https://www.algoexpert.io/questions/Single%20Cycle%20Check

# Time Complexity: O(N) and Space: O(1) 

def get_next_id(current_id, array):
	num_jumps = array[current_id]
	next_up_id = (current_id + num_jumps)%(len(array))
	return next_up_id 
def hasSingleCycle(array):
    # Write your code here.
	aux_array = [False for _ in range(0, len(array))]
	num_elements_visited = 0
	current_id = 0
	while num_elements_visited < len(array):
		if num_elements_visited > 0 and current_id ==0:
			return False
		num_elements_visited += 1
		current_id = get_next_id(current_id, array)
	
    return current_id == 0
