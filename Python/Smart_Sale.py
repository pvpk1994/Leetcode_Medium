# Roblox Interview Coding Question
# Smart Sale 
# Author: Pavan Kumar Paluri
from collections import Counter 
def delete_products(ids:list, m:int)->int:
	# O(NlogN)
	# base conditions
	if len(ids)==0:
		return 0
	ids = sorted(ids)
	tup_ids = Counter(ids).most_common()
	# tuple generation
	while m >= tup_ids[-1][1]:
		m = m-tup_ids[-1][1]
		tup_ids.pop()
	return len(tup_ids)

if __name__ == '__main__':
			print(delete_products([1,2,1,1,1], 2))
