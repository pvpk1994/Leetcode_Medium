# Calculate the dot product between two sparse vectors V1 and V2
# Author: Pavan Kumar Paluri

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ans = 0

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        for i in range(0, len(self.nums)):
            if self.nums[i]==0 or vec.nums[i]==0:
                continue
            else:
                self.ans += self.nums[i]*vec.nums[i]
        return self.ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
