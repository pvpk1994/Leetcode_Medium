# Array Nesting = LeetCode medium 
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        maximum = 0
        
        for i in range(len(nums)):
            # as nums[i] have been seen, you already measure
            # the set of numbers having nums[i]
            if seen[i]:
                continue
                
            total = 1
            seen[i] = True
            k = nums[i]
            
            while not seen[k]:
                total += 1
                seen[k] = True
                k = nums[k]
            
            maximum = max(maximum, total)
            
            # Just an small optimization, if maximum is at least
            # half of size of the array, you know it is the maximum
            # But without having this optimization, algorithm is
            # still O(N)
            if maximum >= len(nums) / 2:
                return maximum
        return maximum
