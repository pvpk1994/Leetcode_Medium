# Author: Pavan Kumar Paluri
# LeetCode Medium - Google Question
# Using Stack Approach 
# Problem Link: https://leetcode.com/problems/find-permutation/
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        final_arr=[]
        for i in range(0, len(s)):
            if s[i]=="D":
                stack.append(i+1)
                if i+1 == len(s):
                    # print(i+2)
                    stack.append(i+2)
                    while len(stack)!=0:
                        elem = stack.pop()
                        final_arr.append(elem)
            elif s[i] == "I":
                stack.append(i+1) 
                while len(stack)!=0:
                    elem = stack.pop()
                    final_arr.append(elem)
                if i+1 == len(s):
                    final_arr.append(i+2)
        return final_arr
       
