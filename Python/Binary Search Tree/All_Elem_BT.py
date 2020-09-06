# Question: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Author: Pavan Kumar Paluri

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity is O(N+M) - linear Pass 
    # Using inorder to keep the arrays sorted in non-decreasing order 
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1= []
        stack2= []
        if root1 is None and root2 is None:
            return []
        output1= []
        output2 = []
        output = []
        # inorder: [left, root, right]
        while stack1 or root1:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            current = stack1.pop()
            output1.append(current.val)
            root1 = current.right
            
        while stack2 or root2:
            while root2:
                stack2.append(root2)
                root2 = root2.left
            current = stack2.pop()
            output2.append(current.val)
            root2 = current.right
        
        # print(output1)
        # print(output2)
        while len(output1)>0 and len(output2)>0:
            if output1[0] < output2[0]:
                elem = output1.pop(0)
                output.append(elem)
            else:
                elem = output2.pop(0)
                output.append(elem)
        # if here: one of the list is empty
        return output+output1 if len(output1)>0 else output+output2
