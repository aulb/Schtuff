"""
  *
 ***
*****
"""

def pyramid(num_rows, left=False):
	if not num_rows: return ""

	pyramid = ""

	for i in range(1, num_rows + 1):
		stars = i * 2 - 1
		spaces = (num_rows - i) * (2 if left else 1)
		pyramid += "{}{}\n".format(spaces * " ", stars * "*")

	return pyramid

if __name__ == '__main__':
	print(pyramid(0))
	print(pyramid(10, True))
	print(pyramid(10))
