import sys
INT_MAX = sys.maxsize
INT_MIN = sys.maxsize * -1

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# TODO: check
def is_bst(node, minimum, maximum):
	# If at the end
	if not node:
		return True

	# node.data needs to be in between
	if not (minimum < node.data < maximum):
		return False

	# left side needs to be lesser than node.data, max = node.data
	# right side needs to be more than node.data, min = node.data
	return is_bst(node.left, minimum, node.data) and is_bst(node.right, node.data, maximum)
