# Calculate Maximum XOR of two numbers in an array 
# Time complexity should not exceed O(N) 
# LeetCode Medium 
# Problem: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Prefixes using hash-set O(32*n) ~ O(N) time complexity
        mask, output = 0, 0
        # Enumerate through the possible two powers
        for i in range(32, -1, -1):
            mask = mask | 1<< i
            uniq_set = set([n&mask for n in nums])
            temp = output | 1<<i
            for elem in uniq_set:
                if elem^temp in uniq_set:
                    output = temp
        return output
