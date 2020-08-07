# Author: Pavan Kumar Paluri
# Search in a rotated array - level 2 (with duplicates)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # convert list into a set
        hash_set = set()
        for num in nums:
            if num in hash_set:
                continue
            else:
                hash_set.add(num)
        nums = list(hash_set)
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[low]:
                if (target < nums[mid] and nums[low] <= target):
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target <= nums[high] and nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
        return False 
