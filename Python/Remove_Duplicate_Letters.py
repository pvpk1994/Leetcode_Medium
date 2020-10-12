# Remove Duplicate Letters
# AUhtor: pavan Kumar Paluri
# Leetcode: https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        pos = 0
        for i in range(0,len(s)):
            # Update pos when s[i] < s[pos]
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''
