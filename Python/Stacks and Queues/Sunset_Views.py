# Sunset Views using Concept of Stacks
# Time and Space Complexity: O(N) and O(N)
# Algo Expert Question: https://www.algoexpert.io/questions/Sunset%20Views
# Author: Pavan Kumar Paluri

def sunsetViews(buildings, direction):
    # Write your code here.
	stack = []
	indices=[]
	if direction == "EAST":
		for i in range(len(buildings)-1, -1, -1):
			if len(stack):
				if buildings[i] > stack[-1]:
					stack.pop()
					stack.append(buildings[i])
					indices.append(i)
			else:
				stack.append(buildings[i])
				indices.append(i)
		return indices[::-1]
	elif direction == "WEST":
		for i in range(0, len(buildings), 1):
			if len(stack):
				if buildings[i] > stack[-1]:
					stack.pop()
					stack.append(buildings[i])
					indices.append(i)
			else:
				stack.append(buildings[i])
				indices.append(i)
		return indices
