import re

def myAtoi(str):
	"""
	:type str: str
	:rtype: int
	"""
	result = 0
	digits = re.compile('[0-9]')
	negFlag = False
	for i in str:
		if digits.match(i):
			result = result * 10 + int(i)
		elif not negFlag and i is '-':
			negFlag = True
	if negFlag:
		result = result * -1
	return result

# Overflow with Python?	        
# If not in [0-9] ignored, except '-'
