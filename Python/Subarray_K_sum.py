# Using Hashmap to store summ
# LeetCode Medium 
# Question: https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count  =0
        summ = 0
        hash_map  = {0:1}
        for i in range(0, len(nums)):
            summ += nums[i]
            if summ-k in hash_map.keys():
                count += hash_map[summ-k]
            hash_map[summ] = hash_map.get(summ, 0)+1
        return count 
