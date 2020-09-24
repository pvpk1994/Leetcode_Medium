# Digit combinations of a phone number
# Author: Pavan Kumar Paluri

class Solution:
	def __init__(self):
		self.hash_map = {"2":"abc", "3":"def", "4":"ghi"}
		self.output = []
	def letter_combo(self, digits:str):
		def helper(letter, digits):
			if len(digits) == 0:
				self.output.append(letter)
				return
			for character in self.hash_map[digits[0]]:
				helper(letter+character, digits[1:])
		helper("", digits)
		print(self.output)

if __name__ == '__main__':
	sol = Solution()
	sol.letter_combo("24")

