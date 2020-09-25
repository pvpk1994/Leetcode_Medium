# Find the Majority Element: Such that the element appears more than floor(len(list)/3) times
# Requirement: Linear O(N) time complexity and O(1) Space complexity
# Author: Pavan Kumar Paluri

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1,can2 =  None, None
        c1,c2 = 0,0
        for i in range(len(nums)):
            if can1==nums[i]:
                c1+=1
            elif can2==nums[i]:
                c2+=1
            elif c1==0:
                # reset the candidate element
                can1=nums[i]
                c1+=1
                # print(can1)
            elif c2==0:
                can2=nums[i]
                c2+=1
                # print(can2)
            else:
                c1+=-1
                c2+=-1
        # print(can1, can2)
        # Second Pass - to verify 
        result = []
        c11,c22=0,0
        for i in range(len(nums)):
            if nums[i]==can1:
                c11+=1
            elif nums[i]==can2:
                c22+=1
        if c11 > math.floor(len(nums)/3):
            result.append(can1)
        if c22 > math.floor(len(nums)/3):
            result.append(can2)
        return result
