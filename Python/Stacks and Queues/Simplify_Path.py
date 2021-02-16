# Simplify Path 
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/simplify-path/
# Time Complexity: O(N) and Space Complexity: O(N)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        list_sep = path.split('/')
        for content in list_sep:
            if content == "..":
                if stack:
                    # pop the top most element out of the stack
                    stack.pop()
            elif content == "." or not content:
                # make no change
                continue
            else:
                stack.append(content)
        f_str = "/" + "/".join(stack)
        return f_str
