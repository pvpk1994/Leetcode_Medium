import math
# OA interview question 
# Brute Force approach - O(N*k)
# Que Data Structure - O(N)
# Author: Pavan Kumar Paluri

# O(N**k) approach 
def brute_force_slider(arr: list, k: int):
	if k == 1:
		return max(arr)
	final_list = []
	for i in range(len(arr)-k+1):
		min_num = math.inf
		for j in range(i, i+k):
			if min_num > arr[j]:
				min_num = arr[j]
		final_list.append(min_num)
	return max(final_list)

# O(N) approach is to use a Queue:
def que_slider(arr: list, k: int):
	list_k = [-1]*k
	for i in range(k):
		# load first k elements into the list_k
		list_k[i] = arr[i]
	# compute the min of the list
	list_min =[]
	list_min.append(min(list_k))
	for i in range(k, len(arr)):
		list_k.pop(0)
		list_k.append(arr[i])
		list_min.append(min(list_k))
	return max(list_min)




if __name__=="__main__":
	# Test cases :
	n = 5
	# arr= [2,5,4,6,8]
	# arr=[1,2,3,1,2]
	# arr=[121, 91, 81, 75, 43, 2, 39]
	# arr=[1,2,3]
	arr=[1,2,3,4,5]
	k = 2
	print(brute_force_slider(arr, k))
	print(que_slider(arr, k))
