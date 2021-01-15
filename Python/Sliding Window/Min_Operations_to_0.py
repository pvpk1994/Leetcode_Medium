# Minimum Number of operations required to reduce the target to 0.
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Time Complexity: O(N) Sliding window and Space Complexity: O(1)

# Depth First Search : Time Limit Exceeded
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        op = math.inf
        start = 0
        end = len(nums)-1
        def depth_first_search(start, end, target):
            nonlocal op
            # If target is reached
            if target ==0:
                op=min(op, len(nums)-(end-start+1))
            # invalid conditions
            if target < 0 or end < start or len(nums)-(end-start+1) >=op:
                return
            depth_first_search(start+1, end, target-nums[start])
            depth_first_search(start, end-1, target-nums[end])
        depth_first_search(start, end, x)
        return op if op != math.inf else -1
        '''
        # to find the min operations to achieve a traget == largest subarray with diff = sum(nums)-x
        n= sum(nums)
        left = 0
        right = 0
        current = 0
        maximum = -1
        for right in range(0, len(nums)):
            current += nums[right]
            while current > n-x and left <= right:
                # remove current element from sum and increment left
                current = current - nums[left]
                left +=1
            if current == n-x:
                maximum = max(maximum, right-left+1)
        return (len(nums)-maximum) if maximum!= -1 else -1
