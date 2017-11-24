def diameter(node):
	best = 1
	def depth(node):
		if not node: return 0
		left = depth(root.left)
		right = depth(root.right)
		best = max(best, left + right + 1)
		return 1 + max(left, right)
	depth(node)
	return best - 1 # uncount one
