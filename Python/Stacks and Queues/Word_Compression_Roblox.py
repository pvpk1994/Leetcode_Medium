# Remove All adjacent duplicates in a string - Level II
# Concept using Stacks
# LeetCode Medium
# Roblox Interview Question

# Question: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# Solution:

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Using stacks, this is possible
        stack =[]
        for character in s:
            if stack and character == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([character,1])
        final_res = ""
        for count, character in stack:
            final_res += character*count 
        return final_res
