class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		# Cycle detection
		seen = {}

		digits = n
		while not seen.get(str(digits), False):
			# Put n in seen
			seen[str(digits)] = True
			result = 0
			for digit in str(digits):
				result += int(digit) ** 2

			if result == 1: return True
			digits = result
			
		# Cycle
		return False
