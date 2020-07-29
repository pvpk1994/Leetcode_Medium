# Author: Pavan Kumar Paluri
# Concept: Backtracking Appraoch

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs of paranthesis -> n open and n close brackets
        output_list = []
        def helper(no_pairs, open_br_count, close_br_count, string):
            if len(string) == 2*no_pairs:
                output_list.append(string)
            if open_br_count < no_pairs:
                helper(no_pairs, open_br_count+1, close_br_count, string+"(")
            if close_br_count < open_br_count:
                helper(no_pairs, open_br_count, close_br_count+1, string+")")
        helper(n, 0, 0, "")
        return output_list
 
