# Its symmetric if the childrens are also symmetric
# Need to check via BFS
# Simplified
def is_sym(left, right):
	if left and right and left.val == right.val:
		return is_sym(left.left, right.right) and is_sym(left.right, right.left)
	return left == right # Works

def isSymmetric(root):
	# # That means we are at the very bottom, return True
	# # 0 - 1 node trees are always symmetrical
	# if (not root.left and not root.right):
	# 	return True
	# # If root.left and root.right present, recursively go in and check
	# if root.left and root.right:
	# 	return isSymmetric(root.left) and isSymmetric(root.right)
	# # Otherwise, this tree is bogus, one of the child missing
	# return False
	return is_sym(root, root)

# Iterative solution
# def iter_is_sym(root):
	# Use a stack/queue
