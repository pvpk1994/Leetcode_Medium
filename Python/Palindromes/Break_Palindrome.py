# Break A Palindrome
# Auhtor: Pavan Kumar Paluri
# LeetCode Question: https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # break a pal
        for i in range(0, len(palindrome)//2):
            # If a non 'a' encountered in any pos of first half of pal, replace it with 'a'
            if palindrome[i] != 'a':
                return palindrome[:i]+'a'+palindrome[i+1:]
            else:
                continue
        # if all were 'a's in first half of string: replace last 'a' with 'b' to get lexicographically smallest non-pal string
        return palindrome[:-1]+'b' if len(palindrome)>1 else ""
