# Beautiful Arrangement using Backtracking 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/beautiful-arrangement/
# Time Complexity: O(P) # P is the Number of Valid Permutations
# Space Complexity: Recursion Stack + List of elements O(RS+N) {RS: Recursion Stack, N: Number of elements in List}

# Backtracking using 
class Solution:
    def __init__(self):
        self.result_count = 0
    def countArrangement(self, n: int) -> int:
        list_output=[]
        # result_count =0
        given_list = []
        for i in range(1, n+1):
            given_list.append(i)
        st_i =0
        end_i = len(given_list)
        def bt(given_list, st_i, end_i):
            if st_i==end_i:
                self.result_count += 1
            else:
                for k in range(st_i, end_i):
                    given_list[k], given_list[st_i] = given_list[st_i], given_list[k]
                    if given_list[st_i]%(st_i+1) == 0 or (st_i+1)%given_list[st_i]==0:
                        bt(given_list, st_i+1, end_i)
                    given_list[k], given_list[st_i] = given_list[st_i], given_list[k]
        bt(given_list, st_i, end_i)
        #print(list_output)
        return self.result_count 
