# Clone Graph - BFS
# Author: Pavan Kumar Paluri

# https://leetcode.com/problems/clone-graph/

# Code:

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# BREADTH FIRST SEARCH - O(M+N), O(N) 
class Solution:
    def __init__(self):
        self.nodes_visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        # Init the queue with given node
        q = deque([node,])
        # clone this particular node and add it to visited list
        clone_node = Node(node.val, [])
        self.nodes_visited[node] = clone_node
        
        while q:
            noder = q.popleft()
            for n in noder.neighbors:
                if n not in self.nodes_visited:
                    self.nodes_visited[n] = Node(n.val, [])
                    q.append(n)
                # add cloned node's neighbor
                self.nodes_visited[noder].neighbors.append(self.nodes_visited[n])
        
        return self.nodes_visited[node]
