# Find the Most competitive Subsequnce given the size of the subsequence 
# Author: Pavan Kumar Paluri
# Using Greedy Approach + Queues
# Leetcode Question: https://leetcode.com/problems/find-the-most-competitive-subsequence/solution/
# Time Complexity: Worst Case: O(N^2) and Avg Case + Best Case: O(N), Space: O(N) for queue

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        num_elem_drop = len(nums)-k
        que = deque([nums[0],])
        for i in range(1, len(nums)):
            while que and que[-1] > nums[i] and num_elem_drop > 0:
                # pop the element of que
                que.pop()
                num_elem_drop -=1
            que.append(nums[i])
        # print(list(que))
        l =list(que)
        return l[:k] 
