# Coding Interview Question
# Backtracking Approach
# Author: Pavan Kumar Paluri

def count_options(num_persons:int, num_groups:int)->list:
	list_grp= []
	final_list= []
	def helper(num_groups, list_grp, start, summ):
		# using backtracking
		# Stopping conditions..
		if summ <0 or len(list_grp)>num_groups:
			return 
		if summ==0 and len(list_grp)==num_groups:
			list_grp = sorted(list_grp[:])
			if list_grp not in final_list:
				final_list.append(sorted(list_grp[:]))
		for i in range(1,num_persons):
			list_grp.append(i)
			helper(num_groups, list_grp, start, summ-i)
			list_grp.pop()

	summ = num_persons
	helper(num_groups, [], 0,summ)
	return (final_list)


if __name__=="__main__":
	num_persons = int(input("Enter the number of persons: "))
	num_groups = int(input("Enter the number of groups: "))
	print(count_options(num_persons, num_groups))
