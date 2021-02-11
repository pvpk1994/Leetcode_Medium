# Longest Harmonic Subsequnce 
# Author: Pavan Kumar Paluri
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # longest harmonic subsequence - O(N*2)
        # Space complexity: O(1)
        # TLE
        # result = 0
        # for i in range(0, len(nums)):
        #     count = 0
        #     flag = False
        #     for j in range(0, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #         elif nums[j]+1 == nums[i]:
        #             count +=1
        #             flag = True
        #     if flag:
        #         result  = max(result, count)
        # return result 
        
        # Approach - 2: Using HashMap
        h_map = defaultdict(int)
        for num in nums:
            h_map[num] += 1
        counter = 0
        result = 0
        for num in h_map.keys():
            if num+1 in h_map:
                result = max(result, h_map[num]+h_map[num+1])
        return result 
