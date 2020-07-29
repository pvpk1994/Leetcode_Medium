# Author: Pavan Kumar Paluri
# Leetcode Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        output_list  = []
        current = root
        def helper(current, output_list, target_sum, inter_list, summ):
            # stopping conditions
            # if target_sum == summ:
            #     print(inter_list)
            #     output_list.append(inter_list)
            # if summ> target_sum:
            #     return
                
            if current is not None:
                inter_list=inter_list+[current.val]
                # print(inter_list)
                summ += current.val
                # Make sure we hit the target sum only at the leaf nodes...
                if target_sum == summ and current.left is None and current.right is None:
                    print(inter_list)
                    output_list.append(inter_list)
                '''
                if summ > target_sum:
                    return
                    '''
                # print(summ)
                if current.left is not None:
                    helper(current.left, output_list, target_sum, inter_list, summ)
                if current.right is not None:
                    helper(current.right, output_list, target_sum, inter_list, summ)
        
        helper(current, output_list, sum, [], 0)
        return output_list
 
