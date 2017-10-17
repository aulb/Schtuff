# TODO: BST today
def vertical_print(node):
	levels = {}

	def add_level(node, position):
		if not node: return

		level = levels.get(position, [])
		level.append(node.val)

		add_level(node.left, position - 1)
		add_level(node.right, position + 1)

	add_level(node, 0)
	return levels
print(levels)
