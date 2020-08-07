# Do a vertical order traversal - using co-ordinate axis 
# Author: Pavan Kumar Paluri
from collections import deque
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        list_nodes = []
        
        def breadth_first_search(root):
            # Que content: (node, row#, col#)
            que = deque([(root, 0, 0)])
            while que:
                # tuple
                noder, row, col = que.popleft()
                if noder is not None:
                    list_nodes.append((col, row, noder.val))
                    # Explore left and right nodes
                    que.append((noder.left, row+1, col-1))
                    que.append((noder.right, row+1, col+1))
        
        # invoke function
        breadth_first_search(root)
        # if here, sort the list now
        list_nodes = sorted(list_nodes)
        print(list_nodes)
        
        result = {}
        for col, row, val in list_nodes:
            if col in result.keys():
                result[col].append(val)
            else:
                # add the val to the list 
                result[col] =[val]
        return result.values()
