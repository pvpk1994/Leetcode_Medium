# Clone Graph
# Author Pavan KUmar Paluri

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# DEPTH FIRST SEARCH - O(M+N), O(N)
class Solution:
    def __init__(self):
        self.nodes_visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Using depth first search - DFS
        if node is None:
            return node
        
        if node not in self.nodes_visited:
            clone_node = Node(node.val, [])
            self.nodes_visited[node] = clone_node
        else: # if node in visited set of nodes 
            return self.nodes_visited[node]
        # iterate through the neighbors of the current node
        if node.neighbors is not None:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node 
