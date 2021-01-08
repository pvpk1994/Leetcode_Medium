# Delete Tree Nodes using graphs
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/delete-tree-nodes/
# Time Complexity: O(N) 
# Depth First Search 
# Space Complexity: O(N) for recursion stack 
class Solution:
    def __init__(self):
        # to keep track of num of deleted nodes 
        self.ans = 0
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        h_map = defaultdict(list)
        for i in range(0, len(parent)):
            h_map[parent[i]].append(i)
        def dfs(h_map, value, root):
            count = 1
            total = value[root]
            for node in h_map[root]:
                c_tot, c_count = dfs(h_map, value, node)
                total = total+c_tot
                count = count+c_count
            if total ==0:
                self.ans += count
                count = 0
            return total, count 
            
        dfs(h_map, value, 0)
        return nodes-self.ans 
