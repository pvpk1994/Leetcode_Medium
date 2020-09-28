# Evaluate Division using DFS
# Problem : LeetCode: https://leetcode.com/problems/evaluate-division/
# Author: Pavan Kumar Paluri

# This problem can also be approached by Union-Find Algorithm

class Solution:
    def backtracking(self, graph, current_node, dest_node, acc_prod, visited):
        visited.add(current_node)
        ret = -1.0
        neighbors = graph[current_node]
        if dest_node in neighbors:
            ret = acc_prod*neighbors[dest_node]
        else:
            for neighbor, value in neighbors.items():
                # if neighbor is already visited 
                if neighbor in visited:
                    continue
                ret = self.backtracking(graph, neighbor, dest_node, acc_prod*value, visited)
                if ret != -1.0:
                    break
        visited.remove(current_node)
        return ret 
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        # Step-1: Build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and bi-directional edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1/value
        
        # Step-2: Evaluate each query using backtracking approach 
        results = []
        for dividend, divisor in queries:
            # exceptions include : if divisor == dividend (OR) if divisor/ dividend does not exist in the graph
            if dividend not in graph or divisor not in graph:
                # either nodes dont exist: return -1
                ret = -1.0
            elif dividend == divisor: 
                ret = 1.0
            else:
                # include the visited nodes in the set 
                visited = set()
                ret = self.backtracking(graph, dividend, divisor, 1, visited)
            results.append(ret)
        return results 
