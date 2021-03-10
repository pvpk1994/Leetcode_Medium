# BFS classes 
# TC: O(V+E) SC:O(V)
# AlgoExpert Question: https://www.algoexpert.io/questions/Breadth-first%20Search
# Author: Pavan Kumar Paluri

from collections import deque
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        que = deque([self])
		while len(que) > 0:
			node = que.popleft()
			array.append(node.name)
			for child in node.children:
				que.append(child)
		return array
