# Balanced Brackets using Stacks
# Time and Space Complexity: O(N) and O(N)
# Author: Pavan Kumar Paluri
# Algo Expert Question: https://www.algoexpert.io/questions/Balanced%20Brackets

def balancedBrackets(string):
    # Write your code here.
	h_map = {']':'[', '}':'{', ')':'('}
	accept_chars = {'{','}','[',']','(',')'}
	stack = ['*']
	for i in range(0, len(string)):
		if string[i] in accept_chars and string[i] not in h_map:
			# simply insert
			stack.append(string[i])
		elif string[i] in accept_chars and string[i] in h_map: # if in h_map
			if stack[-1] == h_map[string[i]]:
				# well and good
				stack.pop()
			else:
				return False
	return stack[-1] == '*'
