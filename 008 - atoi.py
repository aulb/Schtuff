import re

def myAtoi(str):
	"""
	:type str: str
	:rtype: int
	"""
	# NO.
	# result = 0
	# digits = re.compile('[0-9]')
	# negFlag = False
	# for i in str:
	# 	if digits.match(i):
	# 		result = result * 10 + int(i)
	# 	elif not negFlag and i is '-':
	# 		negFlag = True
	# if negFlag:
	# 	result = result * -1
	# return result

# Lots of cases
def ascii_to_integer(ascii_string):
    is_negative = False 
    if len(str) > 0 and str[0] == '-':
        is_negative = True
        str = str[1:]
    result = 0
    offset = ord('0') 
    for char in str: 
        result = result * 10 + (ord(char) - offset)
    return result * (-1 if is_negative else 1)

# Overflow with Python?	        
# If not in [0-9] ignored, except '-'
